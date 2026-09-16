from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from pypinyin import lazy_pinyin

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def _contains_chinese(text):
    return any("\u4e00" <= char <= "\u9fff" for char in text)


def _search_city(city, language):
    search_terms = [city]

    if _contains_chinese(city):
        pinyin_name = "".join(lazy_pinyin(city))
        if pinyin_name and pinyin_name.lower() != city.lower():
            search_terms.append(pinyin_name)

    api_language = "zh" if language == "中文" else "en"

    for search_term in search_terms:
        params = {
            "name": search_term,
            "count": 1,
            "language": api_language,
            "format": "json",
        }
        response = requests.get(GEOCODING_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            return data["results"][0]

    return None


def _weather_key(code):
    if code == 0:
        return "clear"
    if code == 1:
        return "mainly_clear"
    if code == 2:
        return "partly_cloudy"
    if code == 3:
        return "overcast"
    if code in (45, 48):
        return "fog"
    if code in (51, 53, 55):
        return "drizzle"
    if code in (56, 57):
        return "freezing_drizzle"
    if code in (61, 63, 65):
        return "rain"
    if code in (66, 67):
        return "freezing_rain"
    if code in (71, 73, 75):
        return "snow"
    if code == 77:
        return "snow_grains"
    if code in (80, 81, 82):
        return "rain_showers"
    if code in (85, 86):
        return "snow_showers"
    if code == 95:
        return "thunderstorm"
    if code in (96, 99):
        return "thunderstorm_hail"
    return "other"


def get_time_difference(home_offset_seconds, away_offset_seconds):
    return abs(away_offset_seconds - home_offset_seconds) / 3600


def get_weather(city, language="English"):
    try:
        location = _search_city(city, language)
        if location is None:
            return {"status": "not_found", "data": None}

        params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": (
                "temperature_2m,apparent_temperature,precipitation,"
                "weather_code,wind_speed_10m"
            ),
            "daily": "precipitation_probability_max",
            "timezone": "auto",
        }

        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()

        current = weather_data["current"]
        daily = weather_data["daily"]

        timezone_name = weather_data.get("timezone", "UTC")
        local_time = datetime.now(ZoneInfo(timezone_name)).strftime("%H:%M")

        rain_values = daily.get("precipitation_probability_max", [])
        rain_probability = rain_values[0] if rain_values else 0
        if rain_probability is None:
            rain_probability = 0

        return {
            "status": "ok",
            "data": {
                "city": location.get("name", city),
                "country": location.get("country", ""),
                "local_time": local_time,
                "timezone": timezone_name,
                "utc_offset_seconds": weather_data.get("utc_offset_seconds", 0),
                "temperature": current["temperature_2m"],
                "feels_like": current["apparent_temperature"],
                "precipitation": current["precipitation"],
                "wind_speed": current["wind_speed_10m"],
                "weather_key": _weather_key(current["weather_code"]),
                "rain_probability": rain_probability,
            },
        }
    except (requests.RequestException, KeyError, TypeError, ValueError):
        return {"status": "error", "data": None}
