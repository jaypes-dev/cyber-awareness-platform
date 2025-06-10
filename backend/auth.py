from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if not user or not check_password_hash(user.password, request.form['password']):
            return "Invalid"
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = generate_password_hash(request.form['password'])
    new_user = User(email=email, password=password, role='user')
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))
