from .models import User, Session, Specialist, Grant, Subsidy
from . import db
from datetime import datetime


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


def register_user(phone: str, name: str, location: str):
    new_user = User(name=name, phone=phone, location=location)
    db.session.add(new_user)
    db.session.commit()


def update_user(phone: str, name: str, location: str):
    updated_user = User(name=name, phone=phone, location=location)
    db.session.update(updated_user)
    db.session.commit()


def register_specialist(name: str, email: str, phone: str):
    new_specialist = Specialist(name=name, email=email, phone=phone)
    db.session.add(new_specialist)
    db.session.commit()


def all_specialists():
    return Specialist.query.all()


def new_session(mp3_url):
    new_session = Session(enqueue_on=datetime.now(), queryl=mp3_url, status=0)
    db.session.add(new_session)
    db.session.commit()


def confirm_session(id):
    session_to_confirm = Session.query.filter_by(id=id).first_or_404()
    session_to_confirm.status = 1
    session_to_confirm.confirmed_for = datetime.now()
    db.session.commit()


def cancel_session(id):
    session_to_cancel = Session.query.filter_by(id=id).first_or_404()
    session_to_cancel.status = 2
    session_to_cancel.confirmed_for = datetime.now()
    db.session.commit()


def all_session():
    return Session.query.all()


def new_grant(title, description, amount, application_deadline, contact):
    new_grant = Grant(title=title, description=description, amount=amount,
                      application_deadline=application_deadline, contact=contact)
    db.session.add(new_grant)
    db.session.commit()


def new_subsidy(title, description, amount, application_deadline, contact):
    new_subsidy = Subsidy(title=title, description=description, amount=amount,
                          application_deadline=application_deadline, contact=contact)
    db.session.add(new_subsidy)
    db.session.commit()

def time_of_day():
    time_now = datetime.now()

    if time_now.strftime("%p") == "AM":
        return "Good Morning"
    elif int(time_now.strftime("%H")) <= 16:
        return "Good Afternoon"
    else:
        return "Good Evening"
