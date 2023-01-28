import os
from urllib.parse import urlencode
import requests


def send_sms(phone: str, message: str):
    url = os.environ.get(
        'URL', 'https://api.sandbox.africastalking.com/version1/messaging')
    api_key = os.environ.get('API_KEY', '')
    user_name = os.environ.get('USERNAME', 'sandbox')

    data = urlencode({
        "username": user_name,
        "to": phone,
        "message": message,
        "from": os.environ.get('SHORT_CODE', '7633'),
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
