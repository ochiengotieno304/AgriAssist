import os
from urllib.parse import urlencode
from .settings import API_KEY_LIVE, USERNAME
import requests


def initiate_call(from_phone: str, to_phone: str):
    data = urlencode({
        "username": os.getenv('USERNAME'),
        "to": to_phone,
        "from": from_phone
    })

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apiKey": os.getenv('API_KEY_LIVE'),
    }

    res = requests.post(os.getenv('CALL_URL'), data=data, headers=headers)
    if res.status_code != 200:
        print(f"Error placing call: {res.text}")
        return False

    print(f"Call placed {res.text}")

    return True