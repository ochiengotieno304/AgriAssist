from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from .models import User,Grant,Specialist,Session,Subsidy
from .utils import update_user

from . import db

page = Blueprint('page', __name__)

def all_users():
    return User.query.all()



@page.route('/')
@login_required
def index():
    users=all_users()
    return render_template('index.html',users=users)

@page.route('/user/<id>', methods=['POST', 'GET'])
@login_required
def view_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('user.html',user=user)

@page.route('/delete/<id>')
@login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('page.index'))

@page.route('/update/<id>', methods=['POST'])
@login_required
def update_user(id):
    if request.method == 'POST':
        user = User.query.filter_by(id=id).first_or_404()
        user.name = request.form['name']
        user.phone = request.form['phone']
        user.location = request.form['location']
        db.session.update()
        db.session.commit()
        return redirect(url_for('page.index'))

@page.route('/grants')
@login_required
def grants():
    grants = Grant.query.all()
    return render_template('grants.html',grants=grants)

@page.route('/subsidies')
@login_required
def subsidies():
    subsidies = Subsidy.query.all()
    return render_template('subsidies.html',subsidies=subsidies)

@page.route('/specialist')
@login_required
def specialists():
    specialists= Specialist.query.all()
    return render_template('specialists.html',specialists=specialists)

@page.route('/weather')
def weather():
    return render_template('weather.html')
