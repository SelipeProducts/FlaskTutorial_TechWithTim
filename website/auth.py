from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  # data = request.form
  # print(data)
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    #Query db and looking for specific user
    user = User.query.filter_by(email=email).first()

    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully.', category='success')
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect Password.', category='error')
    else:
      flash('Email does not exist.', category='error')

  return render_template('login.html', text='hello', name="Cesar", boolean=True)

@auth.route('/logout')
def logout():
  return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
  if request.method == 'POST':
    email= request.form.get('email')
    firstname = request.form.get('firstname')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email already exists.', category='error')
    elif len(email) < 4:
      flash('Email must be greater than 4 characters.', category='error')
    elif len(firstname) < 2:
      flash('Name must be greater than 2 characters.', category='error')
    elif password1 != password2:
      flash('Passwords do not match.', category='error')
    elif len(password1)< 7:
      flash('Password must be greater than 7 characters.', category='error')
    else:
      #add user to db
      new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method='sha256'))

      #sql commands: add & commit
      db.session.add(new_user)
      db.session.commit()

      flash('Account Created!!!', category='success')
      
      return redirect(url_for('views.home'))
      

  return render_template('sign_up.html')


