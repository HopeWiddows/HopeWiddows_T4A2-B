from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo #importing validators for required data types, validating reall email addresses
from Blog_App import User
#creating classes for different forms on app pages

#registration form
class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)]) #ensuring username is not empty and has character limitations
    email = StringField('Email', validators=[DataRequired(), Email()]) #ensuring email is not empty and is a valid email address
    password = PasswordField('Password', validators=[DataRequired()]) #esuring password is not empty 
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) #ensuring confirmed password is not empty and matches 'password'
    submit = SubmitField('Sign Up') #enalbing submission to the app

#checking if username is already taken, alerting user and requesting new username chosen if true
def validate_username(self, username):
    user = User.query.filterby(username=username.data).first()
    if user:
        raise ValidationError('Oops, that username is already in use. Please try another one to register as a new user.')

#checking if username is already taken, alerting user and requesting new username chosen if true
def validate_email(self, email):
    user = User.query.filterby(email= email.data).first()
    if user:
        raise ValidationError('Oops, that email is already in use. Please use another one to register as a new user.')


#checking if username is already taken, alerting user and requesting new username chosen if true

#log in form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) #ensuring email is not empty and is a valid email address
    password = PasswordField('Password', validators=[DataRequired()]) #esuring password is not empty 
    remember_user = BooleanField('Remember User') #enablign 'remember user' function to remain logged in to app
    submit = SubmitField('Login') #enalbing submission to the app

