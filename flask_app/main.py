from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import login_required, current_user
from . import db

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main.route('/', methods=['GET'])
def landing():
    return render_template('Home.html')

@main.route('/dash', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('Clubs.html', name=current_user.name)

@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('About.html')