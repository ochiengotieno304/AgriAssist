import requests

from .settings import GEOAPIFY_API_KEY, OPENWEATHER_API_KEY


def geocode(location: str):
    url = f"https://api.geoapify.com/v1/geocode/search?text={location}&filter=countrycode:ke&format=json&apiKey={GEOAPIFY_API_KEY}"

    response = requests.get(url)
    parsed = response.json()
    lon = parsed['results'][0]['lon']
    lat = parsed['results'][0]['lat']
    lon = float(f'{lon:.5f}')
    lat = float(f'{lat:.5f}')

    return [lat, lon]

def weather(location: str):
    coordinates = geocode(location)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={OPENWEATHER_API_KEY}&units=metric"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
    
