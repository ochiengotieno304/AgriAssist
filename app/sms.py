import africastalking
from os import getenv
from .settings import USERNAME, API_KEY

def send_sms(message: str, phone: str):
    username = USERNAME
    api_key = API_KEY
    africastalking.initialize(username, api_key)

    sms = africastalking.SMS

    def on_finish(error, response):
        if error is not None:
            raise error
        print(response)

    sms.send(message, [phone], callback=on_finish)
