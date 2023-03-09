from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
import asyncio
from .models import User, Grant, Specialist, Session, Subsidy
from .utils import all_session, register_user, all_users, register_specialist, all_specialists
from .utils import confirm_session, new_grant, new_subsidy, cancel_session, time_of_day
from .sms import send_sms, send_sms_to_all_users

from . import db

page = Blueprint('page', __name__)


@page.route('/')
@login_required
def index():
    users = all_users()
    return render_template('index.html', users=users)


@page.route('/new-user', methods=['POST'])
@login_required
def new_user():
    name = request.form.get('name')
    phone = request.form.get('phone')
    location = request.form.get('location')
    try:
        register_user(phone, name, location)
        return redirect(url_for('page.index'))
    except:
        return redirect(url_for('page.index'))


@page.route('/user/<id>', methods=['POST', 'GET'])
@login_required
def view_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('user.html', user=user)


@page.route('/delete/<id>')
@login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('page.index'))


@page.route('/update-user/<id>', methods=['POST'])
@login_required
def update_user(id):
    user_to_update = User.query.filter_by(id=id).first_or_404()
    if request.method == "POST":
        user_to_update.name = request.form.get('name')
        user_to_update.phone = request.form.get('phone')
        user_to_update.location = request.form.get('location')
        try:
            db.session.commit()
            return redirect(url_for('page.view_user', id=user_to_update.id))
        except:
            return redirect(url_for('page.index'))


@page.route('/grants', methods=['GET', 'POST'])
@login_required
def grants():
    grants = Grant.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        amount = request.form.get('amount')
        application_deadline = request.form.get('deadline')
        contact = request.form.get('contact')

        deadline = datetime.strptime(application_deadline, '%Y-%m-%d').date()
        try:
            new_grant(title, description, amount,
                      deadline, contact)
            flash('Grant added successfully')
            message = f"{time_of_day()}! A new grant is available, kindly contact {contact} for more info before {deadline.strftime('%a %d, %b' )}"
            asyncio.run(send_sms_to_all_users(message))
            return render_template('grants.html', grants=grants)
        except:
            flash('Error adding grant')
            return render_template('grants.html', grants=grants)

    return render_template('grants.html', grants=grants)


@page.route('/subsidies', methods=['POST', 'GET'])
@login_required
def subsidies():
    subsidies = Subsidy.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        amount = request.form.get('amount')
        application_deadline = request.form.get('deadline')
        contact = request.form.get('contact')

        deadline = datetime.strptime(application_deadline, '%Y-%m-%d').date()
        try:
            new_subsidy(title, description, amount,
                        deadline, contact)
            flash('Subsidy added successfully')
            message = f"{time_of_day()}! A new subsidy is available, kindly contact {contact} for more info before {deadline.strftime('%a %d, %b' )}"
            asyncio.run(send_sms_to_all_users(message))
            return render_template('grants.html', subsidies=subsidies)
        except:
            flash('Error adding subsidy')
            return render_template('grants.html', subsidies=subsidies)

    return render_template('subsidies.html', subsidies=subsidies)


@page.route('/new-specialist', methods=['POST'])
@login_required
def new_specialist():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    try:
        register_specialist(name, email, phone)
        return redirect(url_for('page.specialists'))
    except:
        return redirect(url_for('page.index'))


@page.route('/specialist')
@login_required
def specialists():
    specialists = all_specialists()
    return render_template('specialists.html', specialists=specialists)


@page.route('/sessions')
@login_required
def sessions():
    sessions = all_session()
    pending = Session.query.filter(Session.status == 0)
    others = Session.query.filter(Session.status != 0)
    specialists = all_specialists()
    return render_template('sessions.html', sessions=sessions, pending=pending, others=others, specialists=specialists)


@page.route('/cancel-session/<id>')
@login_required
def cancel_sessions(id):
    try:
        cancel_session(id)
        flash('Session cancelled successfully.')
        return redirect(url_for('page.sessions'))
    except:
        flash('Error cancelling session.')
        return redirect(url_for('page.sessions'))


@page.route('/confirm-session/<id>')
@login_required
def confirm_sessions(id):
    try:
        confirm_session(id)
        flash('Session confirmed successfully.')
        return redirect(url_for('page.sessions'))
    except:
        flash('Error confirming session.')
        return redirect(url_for('page.sessions'))


@page.route('/view-session/<id>')
@login_required
def view_session():
    pass


@page.route('/weather')
def weather():
    return render_template('weather.html')
