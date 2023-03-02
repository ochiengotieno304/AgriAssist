import os
from urllib.parse import urlencode
# from .settings import API_KEY, USERNAME, URL, SHORT_CODE
import requests


def voice(from_phone: str, to_phone: str):
    data = urlencode({
        "username": os.getenv('USERNAME'),
        "to": to_phone,
        "from": from_phone,
        # "message": "hello"
    })

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apiKey": os.getenv('API_KEY'),
    }

    res = requests.post(os.getenv('CALL_URL'), data=data, headers=headers)
    if res.status_code != 200:
        print(f"Error placing call: {res.text}")
        return False

    print(f"Call placed {res.text}")
    return res


# voice("+254777888999", "+254777287562")
voice("+254777287562", "+254777888999")
