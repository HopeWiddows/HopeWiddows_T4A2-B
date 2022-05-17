#importing dependencies/libraries
from flask import Flask

#defining app function
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1eaaddc9ac588563a208d46f2098ee7d'

    #importing routes to app files
    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


