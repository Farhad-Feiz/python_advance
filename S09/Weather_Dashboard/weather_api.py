import requests

from config import GEOCODING_API_URL, WEATHER_API_URL


def get_city_coordinates(city_name):

    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        GEOCODING_API_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "country": location.get("country")
    }


def get_weather_description(weather_code):

    weather_codes = {

        0: "Clear Sky",

        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",

        45: "Fog",
        48: "Depositing Rime Fog",

        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",

        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",

        71: "Slight Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",

        80: "Slight Rain Showers",
        81: "Moderate Rain Showers",
        82: "Violent Rain Showers",

        95: "Thunderstorm",

        96: "Thunderstorm with Slight Hail",
        99: "Thunderstorm with Heavy Hail"
    }

    return weather_codes.get(
        weather_code,
        "Unknown Weather"
    )


def get_weather_icon(weather_code):

    weather_icons = {

        0: "☀️",

        1: "🌤️",
        2: "⛅",
        3: "☁️",

        45: "🌫️",
        48: "🌫️",

        51: "🌦️",
        53: "🌦️",
        55: "🌧️",

        61: "🌧️",
        63: "🌧️",
        65: "🌧️",

        71: "🌨️",
        73: "❄️",
        75: "❄️",

        80: "🌦️",
        81: "🌧️",
        82: "⛈️",

        95: "⛈️",

        96: "⛈️",
        99: "⛈️"
    }

    return weather_icons.get(
        weather_code,
        "🌡️"
    )


def get_weather(city_name):

    location = get_city_coordinates(city_name)

    if location is None:
        return None

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code",
        "timezone": "auto"
    }

    response = requests.get(
        WEATHER_API_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    weather_code = data["current"]["weather_code"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "apparent_temperature": data["current"]["apparent_temperature"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "weather_code": weather_code,
        "description": get_weather_description(weather_code),
        "icon": get_weather_icon(weather_code)
    }


if __name__ == "__main__":

    result = get_weather("Kerman")

    print(result)