import os
from urllib.parse import urlencode
from .settings import API_KEY, USERNAME, URL, SHORT_CODE
import requests


def send_sms(phone: str, message: str):
    url = URL
    api_key = API_KEY
    user_name = USERNAME

    data = urlencode({
        "username": user_name,
        "to": phone,
        "message": message,
        "from": SHORT_CODE
    })

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": api_key,
    }

    res = requests.post(url, data=data, headers=headers)
    if res.status_code != 201:
        print(f"Error sending SMS: {res.text}")
        return False

    print("SMS sent successfully")
    return True


send_sms("+254777287562", "hello")
