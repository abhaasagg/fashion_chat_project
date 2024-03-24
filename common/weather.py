import requests


def get_weather(city_name):
    api_key = "39c46f48f0991e8cb96e14ed48de77a3"  # Replace this with your actual API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The current weather in {city_name} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Failed to retrieve weather information. Please check your city name and try again."
