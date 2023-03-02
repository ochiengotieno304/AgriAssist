from .models import User
from . import db


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
