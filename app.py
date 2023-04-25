from flask import Flask, redirect, render_template, request
from src.repositories.user_repository import _user_repo as users
from src.PassHandler import PassHandler
from src.models.models import User, db

global logged_in_user
global logged_in

password_handler = PassHandler()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:mynewpassword@localhost:3306/Forum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
    users.create_user("Todd", "Lewis", "Todd.Lewis@gmail.com",
                      "Tlewyy", users.get_new_user_num(), password_handler.hash_password('password'))


# app = create_app()
logged_in = False


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
            if len(user) > 1:
                if request.form.get('password') != request.form.get('passwordReenter'):
                    return render_template('register.html', error="Username Already Taken")
            logged_in_user = users.create_user(request.form.get('fname'),
                                               request.form.get('lname'), request.form.get('email'), request.form.get('username'), users.get_new_user_num(), password_handler.hash_password(request.form.get('password')))

            global logged_in
            logged_in = True

        else:
            # If user is Logging in

            if not password_handler.verify_password(request.form.get('password'), user[0].password):
                return render_template('login.html', error="Password Invalid")

            logged_in_user = user[0]
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
