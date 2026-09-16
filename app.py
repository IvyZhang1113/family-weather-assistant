import streamlit as st
from recommendations import get_city_advice, get_family_summary
from weather import get_weather, get_time_difference

st.set_page_config(
    page_title="家庭天气",
    page_icon="🌤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

TEXT = {
    "中文": {
        "title": "家庭天气",
        "subtitle": "看看我们两边今天怎么样",
        "city1": "家人 A 的城市",
        "city2": "家人 B 的城市",
        "button": "查看家庭天气",
        "empty": "请输入两个城市。",
        "not_found": "有一个城市没有找到，请检查城市名称。",
        "error": "暂时无法获取天气数据，请稍后重试。",
        "local_time": "当地时间",
        "temperature": "温度",
        "feels_like": "体感",
        "weather": "天气",
        "rain": "今日降雨概率",
        "wind": "风速",
        "time_difference": "时差",
        "temperature_difference": "温差",
        "hours": "小时",
        "summary": "今天两边怎么样",
        "advice": "今天的提醒",
        "umbrella": "雨伞",
        "clothing": "穿衣",
        "weather_text": {
            "clear": "晴朗", "mainly_clear": "大致晴朗",
            "partly_cloudy": "局部多云", "overcast": "阴天",
            "fog": "有雾", "drizzle": "毛毛雨",
            "freezing_drizzle": "冻毛毛雨", "rain": "下雨",
            "freezing_rain": "冻雨", "snow": "下雪",
            "snow_grains": "米雪", "rain_showers": "阵雨",
            "snow_showers": "阵雪", "thunderstorm": "雷暴",
            "thunderstorm_hail": "雷暴伴冰雹", "other": "其他",
        },
    },
    "English": {
        "title": "Family Weather",
        "subtitle": "See how the day feels on both sides",
        "city1": "Family A city",
        "city2": "Family B city",
        "button": "Check Family Weather",
        "empty": "Please enter both cities.",
        "not_found": "One of the cities could not be found.",
        "error": "Weather data is temporarily unavailable.",
        "local_time": "Local time",
        "temperature": "Temperature",
        "feels_like": "Feels like",
        "weather": "Weather",
        "rain": "Rain today",
        "wind": "Wind",
        "time_difference": "Time difference",
        "temperature_difference": "Temperature difference",
        "hours": "hours",
        "summary": "How both sides feel today",
        "advice": "Today's reminders",
        "umbrella": "Umbrella",
        "clothing": "Clothing",
        "weather_text": {
            "clear": "Clear sky", "mainly_clear": "Mainly clear",
            "partly_cloudy": "Partly cloudy", "overcast": "Overcast",
            "fog": "Fog", "drizzle": "Drizzle",
            "freezing_drizzle": "Freezing drizzle", "rain": "Rain",
            "freezing_rain": "Freezing rain", "snow": "Snow",
            "snow_grains": "Snow grains", "rain_showers": "Rain showers",
            "snow_showers": "Snow showers", "thunderstorm": "Thunderstorm",
            "thunderstorm_hail": "Thunderstorm with hail", "other": "Other",
        },
    },
}

# Small mobile-oriented visual polish.
st.markdown("""
<style>
.block-container {max-width: 760px; padding-top: 1.4rem; padding-bottom: 3rem;}
h1 {margin-bottom: .1rem;}
div[data-testid="stMetric"] {
    background: rgba(128,128,128,.07);
    border-radius: 14px;
    padding: 12px;
}
div.stButton > button {border-radius: 12px; min-height: 3rem; font-weight: 600;}
@media (max-width: 640px) {
    .block-container {padding-left: 1rem; padding-right: 1rem;}
    h1 {font-size: 2rem;}
}
</style>
""", unsafe_allow_html=True)

language = st.selectbox("语言 / Language", ["中文", "English"])
t = TEXT[language]

st.title(f"🌤️ {t['title']}")
st.caption(t["subtitle"])

# Streamlit keeps widget values during the active browser session.
# Friendly defaults make first use easier; users can overwrite them.
c1, c2 = st.columns(2)
with c1:
    city1 = st.text_input(t["city1"], value="广州" if language == "中文" else "Guangzhou")
with c2:
    city2 = st.text_input(t["city2"], value="Seattle")

if st.button(t["button"], type="primary", use_container_width=True):
    if not city1.strip() or not city2.strip():
        st.warning(t["empty"])
    else:
        with st.spinner("正在获取天气..." if language == "中文" else "Getting weather..."):
            r1 = get_weather(city1.strip(), language)
            r2 = get_weather(city2.strip(), language)

        statuses = {r1["status"], r2["status"]}
        if "error" in statuses:
            st.error(t["error"])
        elif "not_found" in statuses:
            st.error(t["not_found"])
        else:
            a, b = r1["data"], r2["data"]
            aw = t["weather_text"].get(a["weather_key"], t["weather_text"]["other"])
            bw = t["weather_text"].get(b["weather_key"], t["weather_text"]["other"])

            st.divider()
            left, right = st.columns(2)

            with left:
                st.markdown(f"### 🏠 {a['city']}")
                st.caption(a["country"])
                st.metric(t["temperature"], f"{a['temperature']} °C")
                st.write(f"🕐 **{t['local_time']}：** {a['local_time']}")
                st.write(f"🌡️ **{t['feels_like']}：** {a['feels_like']} °C")
                st.write(f"🌤️ **{t['weather']}：** {aw}")
                st.write(f"☔ **{t['rain']}：** {a['rain_probability']}%")
                st.write(f"💨 **{t['wind']}：** {a['wind_speed']} km/h")

            with right:
                st.markdown(f"### 🌍 {b['city']}")
                st.caption(b["country"])
                st.metric(t["temperature"], f"{b['temperature']} °C")
                st.write(f"🕐 **{t['local_time']}：** {b['local_time']}")
                st.write(f"🌡️ **{t['feels_like']}：** {b['feels_like']} °C")
                st.write(f"🌤️ **{t['weather']}：** {bw}")
                st.write(f"☔ **{t['rain']}：** {b['rain_probability']}%")
                st.write(f"💨 **{t['wind']}：** {b['wind_speed']} km/h")

            st.divider()
            diff_h = get_time_difference(a["utc_offset_seconds"], b["utc_offset_seconds"])
            diff_t = abs(a["temperature"] - b["temperature"])

            m1, m2 = st.columns(2)
            m1.metric(t["time_difference"], f"{diff_h:g} {t['hours']}")
            m2.metric(t["temperature_difference"], f"{diff_t:.1f} °C")

            st.subheader(f"💬 {t['summary']}")
            st.success(get_family_summary(a, b, aw, bw, language))

            st.subheader(f"🧭 {t['advice']}")
            aa_u, aa_c = get_city_advice(a, language)
            bb_u, bb_c = get_city_advice(b, language)
            x, y = st.columns(2)
            with x:
                st.markdown(f"**🏠 {a['city']}**")
                st.info(f"☂️ **{t['umbrella']}：** {aa_u}\n\n👕 **{t['clothing']}：** {aa_c}")
            with y:
                st.markdown(f"**🌍 {b['city']}**")
                st.info(f"☂️ **{t['umbrella']}：** {bb_u}\n\n👕 **{t['clothing']}：** {bb_c}")

st.caption("Weather data: Open-Meteo")
