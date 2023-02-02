from flask import Blueprint, request, render_template, redirect, url_for
from .models import User

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
