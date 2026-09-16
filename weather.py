import requests
from recommendations import get_umbrella_advice, get_clothing_advice

city = input("Enter a city: ")

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

if "results" not in data:
    print("City not found. Please try again.")
    exit()

location = data["results"][0]

city_name = location["name"]
country = location["country"]
latitude = location["latitude"]
longitude = location["longitude"]

weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
    "daily": "precipitation_probability_max",
    "timezone": "auto"
}

weather_response = requests.get(weather_url, params=weather_params)

weather_data = weather_response.json()

current = weather_data["current"]
daily = weather_data["daily"]

temperature = current["temperature_2m"]
feels_like = current["apparent_temperature"]

precipitation = current["precipitation"]
rain_probability = daily["precipitation_probability_max"][0]

umbrella_advice = get_umbrella_advice(rain_probability)
clothing_advice = get_clothing_advice(feels_like)

weather_code = current["weather_code"]
if weather_code == 0:
    weather = "Clear sky"
elif weather_code in [1, 2, 3]:
    weather = "Partly cloudy"
elif weather_code in [45, 48]:
    weather = "Fog"
elif weather_code in [51, 53, 55]:
    weather = "Drizzle"
elif weather_code in [61, 63, 65]:
    weather = "Rain"
else:
    weather = "Other"

wind_speed = current["wind_speed_10m"]


print()
print(city_name + ", " + country)
print("Temperature:", temperature, "°C")
print("Feels like:", feels_like, "°C")
print("Precipitation:", precipitation, "mm")
print("Wind speed:", wind_speed, "km/h")
print("Weather:", weather)
print("Rain probability today:", rain_probability, "%")
print("Advice:", umbrella_advice)
print("Clothing:", clothing_advice)