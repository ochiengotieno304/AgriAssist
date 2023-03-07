from .models import User, Session, Specialist, Grant
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

def new_grant(availability, category):
    new_grant = Grant(availability=availability, category=category)
    db.session.add(new_grant)
    db.session.commit()

