from flask import Blueprint

#defining blueprint for application
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "<h1>Hello</h1>"