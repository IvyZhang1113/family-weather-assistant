def get_umbrella_advice(rain_probability, language="中文"):
    if language == "中文":
        if rain_probability >= 50:
            return "今天建议带伞。"
        if rain_probability >= 30:
            return "有一定降雨可能，带把伞更稳妥。"
        return "今天通常不用带伞。"
    if rain_probability >= 50:
        return "Bring an umbrella today."
    if rain_probability >= 30:
        return "There is some chance of rain; an umbrella may be useful."
    return "An umbrella is probably not needed today."


def get_clothing_advice(feels_like, language="中文"):
    if language == "中文":
        if feels_like >= 30:
            return "天气较热，穿轻薄透气的衣服。"
        if feels_like >= 20:
            return "短袖或轻薄衣物通常比较舒服。"
        if feels_like >= 10:
            return "天气偏凉，建议加一件薄外套。"
        return "天气较冷，注意保暖。"
    if feels_like >= 30:
        return "It is hot; wear light, breathable clothing."
    if feels_like >= 20:
        return "A T-shirt or light layer should be comfortable."
    if feels_like >= 10:
        return "It is cool; a light jacket is useful."
    return "It is cold; wear warm clothing."


def get_city_advice(weather, language="中文"):
    return (
        get_umbrella_advice(weather["rain_probability"], language),
        get_clothing_advice(weather["feels_like"], language),
    )


def get_family_summary(a, b, aw, bw, language="中文"):
    d = abs(a["temperature"] - b["temperature"])
    if language == "中文":
        if b["temperature"] > a["temperature"] + 2:
            compare = f"{b['city']}比{a['city']}暖约 {d:.1f}°C。"
        elif b["temperature"] < a["temperature"] - 2:
            compare = f"{b['city']}比{a['city']}冷约 {d:.1f}°C。"
        else:
            compare = "两边今天温度比较接近。"
        return (
            f"{a['city']}现在{aw}，{a['temperature']}°C；"
            f"{b['city']}现在{bw}，{b['temperature']}°C。{compare}"
        )

    if b["temperature"] > a["temperature"] + 2:
        compare = f"{b['city']} is about {d:.1f}°C warmer than {a['city']}."
    elif b["temperature"] < a["temperature"] - 2:
        compare = f"{b['city']} is about {d:.1f}°C colder than {a['city']}."
    else:
        compare = "Temperatures are fairly similar on both sides today."
    return (
        f"{a['city']} is {aw.lower()} at {a['temperature']}°C; "
        f"{b['city']} is {bw.lower()} at {b['temperature']}°C. {compare}"
    )
