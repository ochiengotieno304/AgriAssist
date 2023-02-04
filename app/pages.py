from flask import Blueprint, request, render_template, redirect, url_for
from .models import User,Grant,Specialist,Session,Subsidy

from . import db

page = Blueprint('page', __name__)

def all_users():
    return User.query.all()



@page.route('/')
def index():
    users=all_users()
    return render_template('index.html',users=users)

@page.route('/user/<id>')
def view_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('user.html',user=user)

@page.route('/delete/<id>')
def delete_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('page.index'))

@page.route('/update/<id>')
def update_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.update(user)
    db.session.commit()
    return redirect(url_for('page.index'))

@page.route('/grants')
def grants():
    grants = Grant.query.all()
    return render_template('grants.html',grants=grants)

@page.route('/subsidies')
def subsidies():
    subsidies = Subsidy.query.all()
    return render_template('subsidies.html',subsidies=subsidies)

@page.route('/specialist')
def specialists():
    specialists= Specialist.query.all()
    return render_template('specialists.html',specialists=specialists)

@page.route('/weather')
def weather():
    return render_template('weather.html')
