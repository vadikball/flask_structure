from flask import Flask

from settings import flask_settings
from .database.postgres.postgres import init_db
from .api.v1.auth import auth


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = flask_settings.secret_key

    app.register_blueprint(auth, url_prefix='/') # register all endpoints for auth service

    init_db() # create tables

    return app
