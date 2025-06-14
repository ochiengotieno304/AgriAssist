from flask import Blueprint, request, render_template
from flask_login import login_required
from .sms import send_sms
from .airtime import send_airtime
from .weather import weather, hourly, daily
from .models import User
from .voice import initiate_call
from .settings import AT_PHONE_NUMBER
from .utils import new_session
from . import db
import asyncio


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


def user_location(phone: str):
    user = User.query.filter_by(phone=phone).first()
    return user.location


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/voice', methods=['POST'])
def voice():
    session_id = request.values.get('sessionID', None)
    is_active = request.values.get('isActive', None)
    recording_url = request.values.get('recordingUrl', None)
    phone = request.values.get('callerNumber', None)

    if find_user(phone):
        if recording_url != None:
            response  = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say> Thankyou, your response has been captured. We will notify you when your session is confirmed</Say>'
            response += '<Reject/>'
            response += '</Response>'
            new_session(recording_url)
        else:
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Record finishOnKey="#" maxLength ="10" trimSilence="true" playBeep="true" >'
            response += f"<Say>Hello {user(phone)}, welcome to AgriAssist. Please describe you query followed by the hash sign after the tone.</Say>"
            response += '</Record>'
            response += '</Response>'
    else:
        response = '<?xml version="1.0" encoding="UTF-8"?>'
        response += '<Response>'
        response += '<Say>Hello, welcome to AgriAssist. Please dial star three eighty four star 76 33 hash to register.</Say>'
        response += '</Response>'

    return response


# TODO seperate menus

@main.route('/ussd', methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        if find_user(phone_number):
            response = f'CON Hello {user(phone_number)}, welcome to AgriAssist \n'
            response += "1. Weather information \n"
            response += "2. Crop information \n"
            response += f"3. Livestock information"

        else:
            response = "CON What would you want to check \n"
            response += "1. Register \n"
            response += "2. More info"

        # registered_options(phone_number, text)

    elif text == '1':
        if find_user(phone_number):
            response = "CON 1. Today (Hourly) \n"
            response += "2. 7-day weather \n"
            response += "3. 30-day weather"
        else:
            response = "CON Enter full name"

    elif text == '2':
        if find_user(phone_number):
            response = "CON Enter your preferred crop \n"
            initiate_call(AT_PHONE_NUMBER, phone_number)
            # TODO send session booking sms
        else:
            response = "END Register for our service to get updates on\n"
            response += "weather and climate patterns"
            response += "alerts on govt subsidies and loans"
            response += "market info"

    elif text == '3':
        if find_user(phone_number):
            response = "CON Enter preferred livestock \n"
            initiate_call(AT_PHONE_NUMBER, phone_number)
            # TODO send session booking sms
        else:
            response = "END Invalid choice, please register"

    elif text == '1*1':
        if find_user(phone_number):
            response = "END We've sent an sms with your request"
            asyncio.run(send_sms(phone_number, hourly(user_location(phone_number))))
        else:
            response = "END Please register"

    elif text == '1*2':
        if find_user(phone_number):
            response = "END We've sent an sms with your request"
            asyncio.run(send_sms(phone_number, daily(user_location(phone_number))))

        else:
            response = "END Please register"

    elif text == '1*3':
        if find_user(phone_number):
            response = "END 30-day"
        else:
            response = "END Please register"

    else:
        arr = text.split("*")
        if len(arr) > 1:
            if find_user(phone_number):
                if arr[0] == "2":
                    crop = arr[1]
                    response = f"END We will call you for more details on your inquiry"

                elif arr[0] == "3":
                    livestock = arr[1]
                    response = f"END We will call you for more details on your inquiry"
                else:
                    response = "END Invalid choice 2"

            else:
                name = arr[1]
                response = "CON Enter Farm Location (Constituency)"
                if len(arr) > 2:
                    location = arr[2]
                    message = f'Dear {name} you have been successfully registered to our service. \n'
                    message += 'Receive info on crop yields, climate patterns, \n'
                    message += 'government grants, loans and other support services \n\n'
                    message += 'For inquiries dial  for more info'
                    try:
                        register_user(phone_number, name, location)
                    except Exception as e:
                        response = f"END Error, try again later \n " + str(e)
                    else:
                        response = f"END Dear {name} you have been successfully registered to our service"
                        asyncio.run(send_sms(phone_number, message))
                        send_airtime(phone_number)
        else:
            response = "END Invalid Choice 3"

    # Send the response back to the API
    return response
