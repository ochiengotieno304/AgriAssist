import africastalking
from .settings import API_KEY

username = "sandbox"
api_key = API_KEY

africastalking.initialize(username, api_key)


def send_airtime(phone_number: str):
    airtime = africastalking.Airtime
    currency_code = "KES"  # Change this to your country's code
    amount = 7

    try:
        response = airtime.send(phone_number=phone_number,
                                amount=amount, currency_code=currency_code)
        print(response)
    except Exception as e:
        print(
            f"Encountered an error while sending airtime. More error details below\n {e}")
