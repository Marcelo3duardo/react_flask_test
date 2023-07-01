import functools
import click

from werkzeug.security import check_password_hash, generate_password_hash

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from api.db import get_db
from api.repository import userRepository
#from api.utils.errors import check_register, check_login

bp = Blueprint('auth', __name__, url_prefix='/')

Users = userRepository()

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = Users.search_id(user_id)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if g.user:
        return jsonify(session)
        #return redirect(url_for('dashboard.dashboard'))
    if request.method == 'POST':
        user_login = request.get_json()

        user = Users.search(user_login['username'])

        error = None

        if user_login['username'] == "":
            error = 'user is required.'
        elif user_login['password'] == "":
            error = 'password is required.'
        elif not check_password_hash(user['password'],user_login['password']):
            error = 'wrong password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return jsonify({"token": session['user_id']})
      

        return jsonify({"error": error})

    #return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({"token": session}),200
    #return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view

@bp.route('/register', methods=('POST','GET'))
def register_user():
    if request.method == 'POST':

        user = request.get_json()
        error = None

        if user['username'] == "":
            error = 'user is required.'
        elif user['fullname'] == "":
            error = 'Fullname is required.'
        elif user['email'] == "":
            error = 'Email is required.'
        elif user['password'] == "":
            error = 'Password is required.'
       
        password = generate_password_hash(user['password'])
        try:
            Users.insert(user['username'],user['fullname'],user['email'],password)
        except:
            error = f"User {user['username']} is already registered."
        if error is None:
            return jsonify(user),200
            #return redirect(url_for("register.users"))
        else:
            #flash(error)
            return jsonify({"error":error})

    return '200'
    #return render_template('register.html')

@bp.route('/users', methods=['GET'])
def users():
    users = Users.get()
    return jsonify(users)

