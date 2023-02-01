import requests
import http.client

from .settings import GEOAPIFY_API_KEY, OPENWEATHER_API_KEY


def geocode(location: str):
    url = f"https://api.geoapify.com/v1/geocode/search?text={location}&filter=countrycode:ke&format=json&apiKey={GEOAPIFY_API_KEY}"

    response = requests.get(url)
    parsed = response.json()
    parsed['results']
    lon = parsed['results'][0]['lon']
    lat = parsed['results'][0]['lat']
    return [lon, lat]


def weather(location: str):
    coordinates = geocode(location)
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={coordinates[1]}&lon={coordinates[0]}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


print(weather('lurambi'))
