from flask import Blueprint, render_template

#defining blueprint for application
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home.html")