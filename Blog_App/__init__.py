from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
#Setting secret key for encryption
app.config['SECRET_KEY'] = '1eaaddc9ac588563a208d46f2098ee7d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #adding database relative path within our project
db = SQLAlchemy(app) #creating database instance

#creating login manager for web app
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from Blog_App import routes

