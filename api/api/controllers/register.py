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
        #username = request.get_json['username']
        #fullname = request.get_json['fullname']
        #email = request.form['email']
        #password = request.form['password']
        user = request.get_json()
        error = None

        if not user:
            error = 'user is required.'
        #elif not fullname:
        #    error = 'Fullname is required.'
        #elif not email:
        #    error = 'Email is required.'
        #elif not password:
        #    error = 'Password is required.'

        #user = (username,fullname,email,password)
        print(user['id'])
        if error is None:
            return jsonify(user)
            repo.insert_user(user['username'],user['fullname'],email,password)
            #return jsonify({"username":username,"fullname":fullname,
            #                "email":email,"password":password}
            #                )
            #return redirect(url_for("register.users"))
        else:
            flash(error)
            return jsonify({"error":error})

    return render_template('register.html')

@bp.route('/users', methods=['GET'])
def users():
    users = repo.list_users()
    return users
    
    #return jsonify(render_template('users.html', users=users))
