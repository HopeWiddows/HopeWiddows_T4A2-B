from flask import Blueprint

#defining blueprint for authorisation 
auth = Blueprint('auth', __name__)

#defining routes to additinal web pages
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"