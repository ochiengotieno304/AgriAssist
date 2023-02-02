from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15), unique=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timedate = db.Column(db.DateTime)
    specialist = db.Column(db.String(100))
    status= db.Column(db.String(100))

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
    phone = db.Column(db.String(15), unique=True)


