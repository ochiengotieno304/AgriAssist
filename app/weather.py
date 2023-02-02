import requests

from .settings import GEOAPIFY_API_KEY, RAPID_API_KEY


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
    url = f"https://forecast9.p.rapidapi.com/rapidapi/forecast/{coordinates[0]}/{coordinates[1]}/hourly/"

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "forecast9.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return response.text


