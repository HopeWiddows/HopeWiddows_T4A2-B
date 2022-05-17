#importing dependencies/libraries
from flask import Flask, flask

#defining app function
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1eaaddc9ac588563a208d46f2098ee7d'

    return app


