from flask import Blueprint, render_template, redirect, url_for, request, flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db
import sqlite3

auth = Blueprint('auth', __name__) # create a Blueprint object that we name 'auth'

@auth.route('/login', methods=['POST']) # define login page path
def login(): # define login page fucntion
    
    email = request.form.get('email')
    email=email.lower() # convert email to lower case to avoid duplicates
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    # check if the user actually exists
    if user==None:
        flash('Please sign up before!', category='warning')
        return redirect(url_for('auth.index'))
    # take the user-supplied password, hash it, and compare it to the hashed password in the database        
    elif not check_password_hash(user.password, password):
        flash('Please check your login details and try again.',category='warning')
        # return redirect(url_for('auth.login')) 
        return redirect(url_for('auth.index'))
    login_user(user, remember=remember)
    return redirect(url_for('main.home'))

@auth.route('/signup', methods=['POST'])# we define the sign up path
def signup(): # define the sign up function
    
    email = request.form.get('email')
    email=email.lower() # convert email to lower case to avoid duplicates
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists',category='warning')
        # return redirect(url_for('auth.signup'))
        return redirect(url_for('auth.index'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256')) #
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    flash('Succesfully registered! Please Login',category='info')
    # return redirect(url_for('auth.login')) # redirects to login
    return redirect(url_for('auth.index')) # redirects to login

@auth.route('/') # home page that return 'index'
def index():
    return redirect('/home')

@auth.route('/logout') # define logout path
@login_required
def logout(): #define the logout function
    logout_user()
    return redirect(url_for('main.home'))
