from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from .models import User, Grant, Specialist, Session, Subsidy
from .utils import all_session, register_user, all_users

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


@page.route('/grants')
@login_required
def grants():
    grants = Grant.query.all()
    return render_template('grants.html', grants=grants)


@page.route('/subsidies')
@login_required
def subsidies():
    subsidies = Subsidy.query.all()
    return render_template('subsidies.html', subsidies=subsidies)


@page.route('/specialist')
@login_required
def specialists():
    specialists = Specialist.query.all()
    return render_template('specialists.html', specialists=specialists)


@page.route('/sessions')
@login_required
def sessions():
    sessions = all_session()
    pending = Session.query.filter(Session.status==0)
    others = Session.query.filter(Session.status!=0)
    return render_template('sessions.html', sessions=sessions, pending=pending, others=others)


@page.route('/view-session/<id>')
@login_required
def view_session():
    pass


@page.route('/weather')
def weather():
    return render_template('weather.html')
