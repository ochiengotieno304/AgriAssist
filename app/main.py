from flask import Blueprint, request, render_template
from .sms import send_sms
from .airtime import send_airtime
from .models import User
from . import db


main = Blueprint('main', __name__)


def register_user(phone: str, name: str, location: str):
    new_user = User(name=name, phone=phone, location=location)
    db.session.add(new_user)
    db.session.commit()


def all_users():
    return User.query.all()


def find_user(phone: str):
    if User.query.filter_by(phone=phone).count() > 0:
        return True


def user(phone: str):
    user = User.query.filter_by(phone=phone).first()
    return user.name


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/voice', methods=['POST'])
def voice():
    session_id = request.values.get('sessionID', None)
    is_active = request.values.get('isActive', None)

    if is_active == 1:
        response = '<?xml version="1.0" encoding="UTF-8"?>'
        response += '<Response>'
        response += '<Say>Please listen to our awesome record</Say>'
        response += '</Response>'

    else:
        duration = request.values.get('durationInSeconds')
        currency_code = request.values.get('currencyCode')
        amount = request.values.get('amount')

    return response


# def registered_options(phone_number, text):
#     if find_user(phone_number):
#         response = f'CON Hello {user(phone_number)}, welcome ... \n'
#         response += "1. Weather information \n"
#         response += "2. Crop information \n"
#         response += "3. Livestock information"
#         if text == '1':
#             response += "1. Today (Hourly) \n"
#             response += "2. 7-day weather \n"
#             response += "3. 30-day weather"

#     else:
#         response = "CON What would you want to check \n"
#         response += "1. Register \n"
#         response += "2. My Phone"

@main.route('/ussd', methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        if find_user(phone_number):
            response = f'CON Hello {user(phone_number)}, welcome ... \n'
            response += "1. Weather information \n"
            response += "2. Crop information \n"
            response += f"3. Livestock information"

        else:
            response = "CON What would you want to check \n"
            response += "1. Register \n"
            response += "2. More info"

        # registered_options(phone_number, text)

    if text == '1':
        if find_user(phone_number):
            response = "CON 1. Today (Hourly) \n"
            response += "2. 7-day weather \n"
            response += "3. 30-day weather"
        else:
            response = "CON Enter full name"

    if text == '2':
        if find_user(phone_number):
            response = "CON Enter your preferred crop \n"
            # TODO send session booking sms
        else:
            response = "END We've sent an sms ..."

    if text == '3':
        if find_user(phone_number):
            response = "CON Enter preferred livestock \n"
            # TODO send session booking sms
        else:
            response = "END Invalid choice, please register"

    else:
        arr = text.split("*")
        if len(arr) > 1:
            name = arr[1]
            response = "CON Enter Farm Location (Constituency)"
            if len(arr) > 2:
                location = arr[2]

                message = f'Dear {name} you have been successfully registered to our service. \n'
                message += 'Receive info on crop yields, climate patterns, \n'
                message += 'government grants, loans and other support services \n\n'
                message += 'For inquiries dial *384*7633# for more info'

                try:
                    register_user(phone_number, name, location)
                except Exception as e:
                    response = f"END Error, try again later \n " + str(e)
                else:
                    response = f"END Dear {name} you have been successfully registered to our service"
                    send_sms(phone_number, message)
                    send_airtime(phone_number)

    # Send the response back to the API
    return response
