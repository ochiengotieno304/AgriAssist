import requests
from time import ctime
from datetime import datetime

# from .settings import GEOAPIFY_API_KEY, OPENWEATHER_API_KEY

GEOAPIFY_API_KEY="79cbac9302a147fd96434ee878451b66"
OPENWEATHER_API_KEY="06bfff4eb1a8e650c9f42d07db5cabd4"

def geocode(location: str):
    url = f"https://api.geoapify.com/v1/geocode/search?text={location}&filter=countrycode:ke&format=json&apiKey={GEOAPIFY_API_KEY}"

    response = requests.get(url)
    parsed = response.json()
    lon = parsed['results'][0]['lon']
    lat = parsed['results'][0]['lat']

    return [lat, lon]

def weather(location: str):
    coordinates = geocode(location)
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={coordinates[0]}&lon={coordinates[1]}&units=metric&appid={OPENWEATHER_API_KEY}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def hourly(location: str):
    response = weather(location)
    hours = response['hourly']
    hourly_weather = "\tTime\t\tTemp\tHumidity\tUVI\n"
    for i in hours:
        date = datetime.fromtimestamp((i['dt'])).strftime("%Y-%m-%d %H:%M")
        hourly_weather += f"{date}\t{i['temp']}\t{i['humidity']}\t\t{i['uvi']}\n"

    return hourly_weather


def daily(location: str):
    response = weather(location)
    days = response['daily']
    daily_weather = "\tDay\t\t\tTemp\t\tHumidity\tUVI\n"
    for i in days:
        date = ctime((i['dt']))
        daily_weather += f"{date}\t{i['temp']['day']}\t\t{i['humidity']}\t\t{i['uvi']}\n"

    return daily_weather
