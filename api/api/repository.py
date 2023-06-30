from api.db import get_db
from werkzeug.security import generate_password_hash

class userRepository:
    def list_users(self):
        db = get_db()
        #return db.execute(
        #    'SELECT * FROM user'
        #).fetchall()
        rows = db.execute(
            'SELECT * FROM user'
        ).fetchall()
        users = []
        for i in rows:
            user = {}
            user["username"] = i["username"]
            user["fullname"] = i["fullname"]
            user["email"] = i["email"]
            user["password"] = i["password"]
            users.append(user)
        return users


    def insert_user(self, username, fullname, email, password):
        db = get_db()
        try:
            db.execute(
                "INSERT INTO user (username, fullname, email, password) VALUES (?, ?, ?, ?)",
                (username, fullname,
                 email, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {username} is already registered."
        return error

    def search(self, username):
        db = get_db()
        return db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

    def search_id(self, user_id):
        return get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
            ).fetchone()
