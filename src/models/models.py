from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)


class Forum(db.Model):
    forum_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    forum_id = db.Column(db.Integer, nullable=False)

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(300), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)