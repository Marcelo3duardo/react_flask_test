import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from api.db import get_db
from api.repository import userRepository

bp = Blueprint('register', __name__, url_prefix='/')

repo = userRepository()

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

        if error is None:
            repo.insert_user(user['username'],user['fullname'],user['email'],user['password'])
            return jsonify(user),200
            #return redirect(url_for("register.users"))
        else:
            #flash(error)
            return jsonify({"error":error})

    return render_template('register.html')

@bp.route('/users', methods=['GET'])
def users():
    users = repo.list_users()
    return users
    
