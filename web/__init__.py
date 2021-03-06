from flask import Flask
from .views import api, load_config


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(api)
    return app

def get_hello():
    return 'hello'

def get_bye():
    return 'bye!'
