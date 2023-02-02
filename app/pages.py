from flask import Blueprint, request, render_template
from .models import User

page = Blueprint('page', __name__)

def all_users():
    return User.query.all()

@page.route('/')
def index():
    users=all_users()
    return render_template('index.html',users=users)

