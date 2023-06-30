import os
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    from . import db
    db.init_app(app)

    #from api.controllers import register
    #app.register_blueprint(register.bp)

    from api.controllers import auth
    app.register_blueprint(auth.bp)

    return app

