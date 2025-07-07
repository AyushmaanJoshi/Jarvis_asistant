import requests

def get_weather(city, api_key):
    """
    Fetches current weather for the specified city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return f"Sorry, I couldn't find weather for {city}."
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    except Exception:
        return "Sorry, I couldn't fetch the weather right now."
