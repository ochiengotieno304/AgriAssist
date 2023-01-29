from flask import Blueprint, request
from .sms import send_sms
import os


main = Blueprint('main', __name__)


@main.route('/ussd', methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        # This is the first request. Note how we start the response with CON
        response = "CON What would you want to check \n"
        response += "1. Register \n"
        response += "2. My Phone"

    elif text == '1':
        response = "CON Enter full name"

    elif text == '2':
        response = "END Your Phone " + phone_number
        send_sms(phone_number, "hello")

    else:
        arr = text.split("*")
        if len(arr) > 1:
            response = "END Your full name" + arr[1]

    # Send the response back to the API
    return response
