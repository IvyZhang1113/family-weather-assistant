import streamlit as st

from recommendations import (
    get_city_advice,
    get_family_summary,
)
from weather import get_weather, get_time_difference

st.set_page_config(
    page_title="Family Weather",
    page_icon="🌍",
    layout="centered",
)

TEXT = {
    "English": {
        "title": "Family Weather",
        "subtitle": "Compare weather and time for family members living in different places.",
        "home_city": "Family's city",
        "away_city": "Other family city",
        "home_placeholder": "e.g. Guangzhou, 北京",
        "away_placeholder": "e.g. Seattle, London",
        "button": "Check Family Weather",
        "empty": "Please enter both cities.",
        "not_found": "One of the cities could not be found. Please check the spelling.",
        "error": "Weather data is temporarily unavailable. Please try again.",
        "family": "Family",
        "student": "Away",
        "local_time": "Local time",
        "temperature": "Temperature",
        "feels_like": "Feels like",
        "weather": "Weather",
        "rain": "Rain today",
        "wind": "Wind",
        "time_difference": "Time difference",
        "temperature_difference": "Temperature difference",
        "hours": "hours",
        "summary": "Family summary",
        "city_advice": "Daily advice",
        "umbrella": "Umbrella",
        "clothing": "Clothing",
        "weather_text": {
            "clear": "Clear sky",
            "mainly_clear": "Mainly clear",
            "partly_cloudy": "Partly cloudy",
            "overcast": "Overcast",
            "fog": "Fog",
            "drizzle": "Drizzle",
            "freezing_drizzle": "Freezing drizzle",
            "rain": "Rain",
            "freezing_rain": "Freezing rain",
            "snow": "Snow",
            "snow_grains": "Snow grains",
            "rain_showers": "Rain showers",
            "snow_showers": "Snow showers",
            "thunderstorm": "Thunderstorm",
            "thunderstorm_hail": "Thunderstorm with hail",
            "other": "Other",
        },
    },
    "中文": {
        "title": "家庭天气",
        "subtitle": "一眼看看住在不同城市的家人今天都怎么样。",
        "home_city": "家里的城市",
        "away_city": "家人所在城市",
        "home_placeholder": "例如：广州、北京",
        "away_placeholder": "例如：Seattle、London",
        "button": "查看家庭天气",
        "empty": "请输入两个城市。",
        "not_found": "有一个城市没有找到，请检查城市名称。",
        "error": "暂时无法获取天气数据，请稍后重试。",
        "family": "家里",
        "student": "另一边",
        "local_time": "当地时间",
        "temperature": "温度",
        "feels_like": "体感",
        "weather": "天气",
        "rain": "今日降雨概率",
        "wind": "风速",
        "time_difference": "时差",
        "temperature_difference": "温差",
        "hours": "小时",
        "summary": "家庭天气总结",
        "city_advice": "今日提醒",
        "umbrella": "雨伞",
        "clothing": "穿衣",
        "weather_text": {
            "clear": "晴朗",
            "mainly_clear": "大致晴朗",
            "partly_cloudy": "局部多云",
            "overcast": "阴天",
            "fog": "有雾",
            "drizzle": "毛毛雨",
            "freezing_drizzle": "冻毛毛雨",
            "rain": "下雨",
            "freezing_rain": "冻雨",
            "snow": "下雪",
            "snow_grains": "米雪",
            "rain_showers": "阵雨",
            "snow_showers": "阵雪",
            "thunderstorm": "雷暴",
            "thunderstorm_hail": "雷暴伴冰雹",
            "other": "其他",
        },
    },
}

language = st.selectbox("Language / 语言", ["English", "中文"])
text = TEXT[language]

st.title(text["title"])
st.caption(text["subtitle"])

col1, col2 = st.columns(2)
with col1:
    home_city = st.text_input(
        text["home_city"],
        placeholder=text["home_placeholder"],
    )
with col2:
    away_city = st.text_input(
        text["away_city"],
        placeholder=text["away_placeholder"],
    )

if st.button(text["button"], type="primary", use_container_width=True):
    if not home_city.strip() or not away_city.strip():
        st.warning(text["empty"])
    else:
        home_result = get_weather(home_city.strip(), language)
        away_result = get_weather(away_city.strip(), language)

        statuses = {home_result["status"], away_result["status"]}

        if "error" in statuses:
            st.error(text["error"])
        elif "not_found" in statuses:
            st.error(text["not_found"])
        else:
            home = home_result["data"]
            away = away_result["data"]

            home_weather = text["weather_text"].get(
                home["weather_key"], text["weather_text"]["other"]
            )
            away_weather = text["weather_text"].get(
                away["weather_key"], text["weather_text"]["other"]
            )

            st.divider()

            left, right = st.columns(2)

            with left:
                st.subheader(f'🏠 {text["family"]}')
                st.markdown(f'### {home["city"]}, {home["country"]}')
                st.write(f'🕐 **{text["local_time"]}:** {home["local_time"]}')
                st.metric(text["temperature"], f'{home["temperature"]} °C')
                st.write(f'**{text["feels_like"]}:** {home["feels_like"]} °C')
                st.write(f'**{text["weather"]}:** {home_weather}')
                st.write(f'**{text["rain"]}:** {home["rain_probability"]}%')
                st.write(f'**{text["wind"]}:** {home["wind_speed"]} km/h')

            with right:
                st.subheader(f'🎓 {text["student"]}')
                st.markdown(f'### {away["city"]}, {away["country"]}')
                st.write(f'🕐 **{text["local_time"]}:** {away["local_time"]}')
                st.metric(text["temperature"], f'{away["temperature"]} °C')
                st.write(f'**{text["feels_like"]}:** {away["feels_like"]} °C')
                st.write(f'**{text["weather"]}:** {away_weather}')
                st.write(f'**{text["rain"]}:** {away["rain_probability"]}%')
                st.write(f'**{text["wind"]}:** {away["wind_speed"]} km/h')

            st.divider()

            time_difference = get_time_difference(
                home["utc_offset_seconds"],
                away["utc_offset_seconds"],
            )
            temperature_difference = abs(
                away["temperature"] - home["temperature"]
            )

            metric1, metric2 = st.columns(2)
            metric1.metric(
                text["time_difference"],
                f'{time_difference:g} {text["hours"]}',
            )
            metric2.metric(
                text["temperature_difference"],
                f'{temperature_difference:.1f} °C',
            )

            summary = get_family_summary(
                home=home,
                away=away,
                home_weather=home_weather,
                away_weather=away_weather,
                language=language,
            )

            st.subheader(f'💬 {text["summary"]}')
            st.success(summary)

            home_umbrella, home_clothing = get_city_advice(home, language)
            away_umbrella, away_clothing = get_city_advice(away, language)

            st.subheader(f'🧭 {text["city_advice"]}')

            advice_left, advice_right = st.columns(2)
            with advice_left:
                st.markdown(f'**🏠 {home["city"]}**')
                st.info(f'☂️ **{text["umbrella"]}:** {home_umbrella}')
                st.info(f'👕 **{text["clothing"]}:** {home_clothing}')

            with advice_right:
                st.markdown(f'**🌍 {away["city"]}**')
                st.info(f'☂️ **{text["umbrella"]}:** {away_umbrella}')
                st.info(f'👕 **{text["clothing"]}:** {away_clothing}')
