# from urllib.parse import urlencode
from .settings import API_KEY, USERNAME, URL, SHORT_CODE
# import requests
import africastalking

username = USERNAME    # use 'sandbox' for development in the test environment
api_key = API_KEY

africastalking.initialize(username, api_key)
sms = africastalking.SMS


# def send_sms(phone: str, message: str):

#     data = urlencode({
#         "username": USERNAME,
#         "to": phone,
#         "message": message,
#         "from": SHORT_CODE
#     })

#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "apiKey": API_KEY
#     }

#     res = requests.post(URL, data=data, headers=headers)
#     if res.status_code != 201:
#         print(f"Error sending SMS: {res.text}")
#         return False

#     print("SMS sent successfully")
#     return True

def send_sms(phone, message):
    response = sms.send(message, [phone])
    print(response)   
