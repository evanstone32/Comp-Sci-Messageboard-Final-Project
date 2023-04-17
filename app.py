from flask import Flask, redirect, render_template, request
from src.repositories.user_repository import get_user_repository


app = Flask(__name__)
global logged_in_user

global logged_in
logged_in = False


users = get_user_repository()

users.create_user("Todd", "Lewis", "Todd.Lewis@gmail.com",
                  "Tlewyy", users.get_new_user_num())
users.get_all_users()[0].set_password('password')


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/login')
def login():
    return render_template('login.html')


@app.get('/forum')
def forum():
    return render_template('forum.html')


@app.get('/register')
def register():
    return render_template('register.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():

    if request.method == 'POST':
        # print(request.form['email'])

        user = users.get_user_by_username(request.form['username'])

        if user is None and request.form['passwordReenter'] is not None:

            global logged_in_user
            logged_in_user = users.create_user(request.form['fname'],
                                               request.form['lname'], request.form['email'], request.form['username'], users.get_new_user_num())
            logged_in_user.set_password(request.form['password'])
            global logged_in
            logged_in = True
        else:
            logged_in_user = user
            logged_in = True

    # else:
    #   user = request.args.get('nm')
    #   return redirect(url_for('success',name = user))

    if not logged_in:
        return redirect("/")

    return render_template('profile.html', user=logged_in_user)


@app.get('/posts')
def create_movies_form():
    return render_template('posts.html')


@app.post('/posts')
def create_movie():
    return redirect('/posts')
