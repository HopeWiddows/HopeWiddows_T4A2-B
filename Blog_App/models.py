#!/usr/bin/env python3

from datetime import datetime
from blog_app import db

#user login manager beign called to load up data
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#creating user model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #setting unique user id column
    username = db.Column(db.String(15), unique=True, nullable=False) #setting username column with its conditions
    email = db.Column(db.String(150), unique=True, nullable=False) #setting email column with its conditions
    profile_image = db.Column(db.String(20), default='default.jpg', nullable=False) #setting profile image column with its conditions
    password = db.Column(db.String(60), nullable=False)#setting password column with its conditions
    posts = db.relationship('Post', backref='author', lazy=True) #creating relationship between the user/author and their posts

    #creating a repr method to return string representation of an object
    def __repr__(self):
        return f"User('{self.username}'),('{self.email}'),('{self.profile_image}')"
    
class Post(db.Model):  
    id = db.Column(db.Integer, primary_key=True) #setting unique post id column
    title = db.Column(db.String(200), nullable=False) #setting post title column with its conditions
    date_posted = db.Column(db.DateTime, default = datetime.utcnow, nullable=False) #setting date posted column with its conditions
    post_content = db.Column(db.Text, nullable=False) #setting post body/content column with its conditions
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)#creating relationship between posts and the user/their author

    #creating a repr method to return string representation of an object
    def __repr__(self):
        return f"User('{self.title}'),('{self.date_posted}')"
