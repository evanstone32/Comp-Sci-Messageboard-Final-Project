from flask import Flask, redirect, render_template, request
from src.repositories.user_repository import get_user_repository
from src.PassHandler import PassHandler

app = Flask(__name__)
password_handler = PassHandler()

global logged_in_user

global logged_in
logged_in = False


users = get_user_repository()

users.create_user("Todd", "Lewis", "Todd.Lewis@gmail.com",
                  "Tlewyy", users.get_new_user_num())
users.get_all_users()[0].set_password(
    password_handler.hash_password('password'))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        global logged_in
        logged_in = False

        global logged_in_user

        del logged_in_user

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

        user = users.get_user_by_username(request.form.get('username'))

        # If user is registering

        if user is None and request.form.get('passwordReenter') is not None:

            if request.form.get('password') != request.form.get('passwordReenter'):
                return render_template('register.html', error="Passwords dont match")

            global logged_in_user
            logged_in_user = users.create_user(request.form.get('fname'),
                                               request.form.get('lname'), request.form.get('email'), request.form.get('username'), users.get_new_user_num())
            logged_in_user.set_password(
                password_handler.hash_password(request.form.get('password')))
            global logged_in
            logged_in = True

        else:
            # If user is Logging in

            if not password_handler.verify_password(request.form.get('password'), user.password):
                return render_template('login.html', error="Password Invalid")

            logged_in_user = user
            logged_in = True

    if not logged_in:
        return redirect("/")

    return render_template('profile.html', user=logged_in_user)


@ app.get('/posts')
def create_movies_form():
    return render_template('posts.html')


@ app.post('/posts')
def create_movie():
    return redirect('/posts')
