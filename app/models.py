from . import db

from . import db
from flask_login import UserMixin


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15), unique=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enqueue_on = db.Column(db.DateTime)
    confirmed_for = db.Column(db.DateTime)
    queryl = db.Column(db.String)
    status = db.Column(db.Integer)

class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.String(100))
    category = db.Column(db.String(100))

class Subsidy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.String(100))
    category = db.Column(db.String(100))

class Specialist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15), unique=True)


