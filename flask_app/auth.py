from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from . import db

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('Log-in.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('name')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(name=username).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.dashboard'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('Sign-up.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(name=name).first()
    
    if user:
        flash('Name already exists')
        return redirect(url_for('auth.signup'))
    
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'), clubs=[])
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))