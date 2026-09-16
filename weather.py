from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import requests
from pypinyin import lazy_pinyin

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def _contains_chinese(text):
    return any("\u4e00" <= char <= "\u9fff" for char in text)


def _search_city(city, language):
    terms = [city]
    if _contains_chinese(city):
        pinyin = "".join(lazy_pinyin(city))
        if pinyin and pinyin.lower() != city.lower():
            terms.append(pinyin)

    api_language = "zh" if language == "中文" else "en"
    for term in terms:
        response = requests.get(
            GEOCODING_URL,
            params={"name": term, "count": 1, "language": api_language, "format": "json"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            return data["results"][0]
    return None


def _weather_key(code):
    groups = {
        "clear": {0}, "mainly_clear": {1}, "partly_cloudy": {2}, "overcast": {3},
        "fog": {45, 48}, "drizzle": {51, 53, 55}, "freezing_drizzle": {56, 57},
        "rain": {61, 63, 65}, "freezing_rain": {66, 67}, "snow": {71, 73, 75},
        "snow_grains": {77}, "rain_showers": {80, 81, 82},
        "snow_showers": {85, 86}, "thunderstorm": {95},
        "thunderstorm_hail": {96, 99},
    }
    for key, codes in groups.items():
        if code in codes:
            return key
    return "other"


def get_time_difference(offset_a, offset_b):
    return abs(offset_b - offset_a) / 3600


def get_weather(city, language="中文"):
    try:
        location = _search_city(city, language)
        if location is None:
            return {"status": "not_found", "data": None}

        response = requests.get(
            FORECAST_URL,
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
                "daily": "precipitation_probability_max",
                "timezone": "auto",
            },
            timeout=10,
        )
        response.raise_for_status()
        raw = response.json()
        current, daily = raw["current"], raw["daily"]

        timezone_name = raw.get("timezone", "UTC")
        local_now = datetime.now(ZoneInfo(timezone_name))
        local_time = local_now.strftime("%H:%M")
        local_date_iso = local_now.strftime("%Y-%m-%d")
        weekday = local_now.weekday()

        rain = daily.get("precipitation_probability_max", [0])
        rain = rain[0] if rain else 0
        rain = 0 if rain is None else rain

        return {
            "status": "ok",
            "data": {
                "city": location.get("name", city),
                "country": location.get("country", ""),
                "local_time": local_time,
                "local_date_iso": local_date_iso,
                "weekday": weekday,
                "timezone": timezone_name,
                "utc_offset_seconds": raw.get("utc_offset_seconds", 0),
                "temperature": current["temperature_2m"],
                "feels_like": current["apparent_temperature"],
                "precipitation": current["precipitation"],
                "wind_speed": current["wind_speed_10m"],
                "weather_key": _weather_key(current["weather_code"]),
                "rain_probability": rain,
            },
        }
    except (requests.RequestException, KeyError, TypeError, ValueError, ZoneInfoNotFoundError):
        return {"status": "error", "data": None}
