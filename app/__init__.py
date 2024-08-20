from flask import Flask, session

def create_app():
    app = Flask(__name__)
    app.secret_key = 'Surubaoderato123#'

    with app.app_context():
        from . import routes

    return app
