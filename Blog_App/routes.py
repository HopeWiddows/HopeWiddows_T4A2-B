#!/usr/bin/env python3
from flask import render_template, url_for, flash, redirect
from blog_app import app
from blog_app.forms import RegForm, LoginForm #importing form data from forms.py
from blog_app.models import User, Post 

#creating list for blog post data
posts = [
    {
        'author': 'Hope 1', 
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 1, 2022'
    },
    {
        'author': 'Hope 2', 
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 2, 2022'
    }
]

 #routing pages to each other
@app.route("/") 
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) #rendering html templates

@app.route("/about")
def about():
    return render_template('about.html', title ='About') #rendering html templates

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account Created for user {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register User', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #validates loging if details are correct and redirects to home page automatically
    if form.validate_on_submit(): 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in.', 'success')
            return redirect(url_for('home'))
        #warns user of incorrect details entered and resets login page
        else: 
            flash('Login Unsuccessfull. Plese check your details and try again.', 'danger')
    return render_template('login.html', title='User Login', form=form)

