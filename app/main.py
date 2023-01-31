from flask import Blueprint, request, render_template
from .sms import send_sms
from .models import User
from . import db


main = Blueprint('main', __name__)


def register_user(phone: str, name: str):
    new_user = User(name=name, phone=phone)
    db.session.add(new_user)
    db.session.commit()


def all_users():
    return User.query.all()


def find_user(phone: str):
    if User.query.filter_by(phone=phone).count() > 0:
        return True

@main.route('/')
def index():
    return render_template('example.html')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/login')
def login():
    return render_template('login.html')
@main.route('/register')
def register():
    return render_template('register.html')
@main.route('/profile')
def profile():
    return render_template('profile.html')
@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@main.route('/navbar')
def navbar():
    return render_template('navbar.html')
@main.route('/users')
def users():
    return render_template('users.html')
@main.route('/sales')
def sales():
    return render_template('sales.html')
@main.route('/websitetraffic')
def websitetraffic():
    return render_template('websitetraffic.html')
@main.route('/password')
def password():
    return render_template('password.html')


@main.route('/ussd', methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        if find_user(phone_number):
            response = 'END Hello, Welcome to ..'
        else:
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
            name = arr[1]
            message = f'''
                Dear {name} you have been successfully registerd to our service.
                Recieve advice on crop switching
                Recieve info on subsidies, loans, and other support services
                Connect with buyers, wholesalers and retailers for your products through our USSD service


                Dial *384*7633# for more info
            '''
            try:
                register_user(phone_number, arr[1])
            except Exception as e:
                response = f"END An error occured try again later \n " + str(e)
            else:
                response = f"END Dear {name} you have been successfully registerd to the service"
                send_sms(phone_number, message)

    # Send the response back to the API
    return response
