def get_umbrella_advice(rain_probability):
    if rain_probability >= 50:
        return "Bring an umbrella."
    else:
        return "Umbrella probably not needed."

def get_clothing_advice(feels_like):
    if feels_like >= 30:
        return "Wear light and breathable clothing."
    elif feels_like >= 20:
        return "A T-shirt or light layer should be comfortable."
    elif feels_like >= 10:
        return "Wear a light jacket."
    else:
        return "Wear warm clothing."