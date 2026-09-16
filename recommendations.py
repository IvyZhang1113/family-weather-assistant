def get_umbrella_advice(rain_probability, language="English"):
    if language == "中文":
        if rain_probability >= 50:
            return "今天建议带伞。"
        if rain_probability >= 30:
            return "有一定降雨可能，带一把伞更稳妥。"
        return "今天通常不需要带伞。"

    if rain_probability >= 50:
        return "Bring an umbrella today."
    if rain_probability >= 30:
        return "There is some chance of rain. An umbrella may be useful."
    return "An umbrella is probably not needed today."


def get_clothing_advice(feels_like, language="English"):
    if language == "中文":
        if feels_like >= 30:
            return "天气较热，建议穿轻薄、透气的衣服。"
        if feels_like >= 20:
            return "短袖或轻薄衣物通常比较舒适。"
        if feels_like >= 10:
            return "天气偏凉，建议加一件薄外套。"
        return "天气较冷，建议穿暖一些。"

    if feels_like >= 30:
        return "It is hot. Wear light and breathable clothing."
    if feels_like >= 20:
        return "A T-shirt or light layer should be comfortable."
    if feels_like >= 10:
        return "It is cool. Wear a light jacket."
    return "It is cold. Wear warm clothing."


def get_city_advice(weather, language="English"):
    umbrella = get_umbrella_advice(weather["rain_probability"], language)
    clothing = get_clothing_advice(weather["feels_like"], language)
    return umbrella, clothing


def get_family_summary(home, away, home_weather, away_weather, language="English"):
    difference = abs(away["temperature"] - home["temperature"])

    if language == "中文":
        if away["temperature"] > home["temperature"] + 2:
            comparison = f"两地温差约 {difference:.1f}°C，第二个城市更暖。"
        elif away["temperature"] < home["temperature"] - 2:
            comparison = f"两地温差约 {difference:.1f}°C，第一个城市更暖。"
        else:
            comparison = "两地今天温度比较接近。"

        return (
            f'{home["city"]}现在{home_weather}，{home["temperature"]}°C；'
            f'{away["city"]}现在{away_weather}，{away["temperature"]}°C。'
            f'{comparison}'
        )

    if away["temperature"] > home["temperature"] + 2:
        comparison = f"The second city is about {difference:.1f}°C warmer."
    elif away["temperature"] < home["temperature"] - 2:
        comparison = f"The first city is about {difference:.1f}°C warmer."
    else:
        comparison = "Temperatures are fairly similar in both cities today."

    return (
        f'{home["city"]} is {home_weather.lower()} at {home["temperature"]}°C; '
        f'{away["city"]} is {away_weather.lower()} at {away["temperature"]}°C. '
        f'{comparison}'
    )
