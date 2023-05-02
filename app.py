from flask import Flask, redirect, render_template, request
from src.repositories.user_repository import _user_repo as users
from src.PassHandler import PassHandler
from src.models.models import User, Forum, Post, Comment, db
from src.repositories.post_repository import _post_repo as posts
from src.repositories.comment_repository import _comment_repo as comment

global logged_in_user
global logged_in

password_handler = PassHandler()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password@localhost:3306/Forum'
    #'mysql://root:mynewpassword@localhost:3306/Forum'
    
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
    forum = Forum.query.all() #not a method call yet
    return render_template('forum.html',forum=forum)


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
            if request.form.get('password') != request.form.get('passwordReenter'):
                return render_template('register.html', error="Username Already Taken")
            logged_in_user = users.create_user(request.form.get('fname'),
                                            request.form.get('lname'), request.form.get('email'), request.form.get('username'), users.get_new_user_num(), password_handler.hash_password(request.form.get('password')))

            global logged_in
            logged_in = True

        else:
            # If user is Logging in

            print(user)

            if not password_handler.verify_password(request.form.get('password'), user.password):
                return render_template('login.html', error="Password Invalid")

            logged_in_user = user
            logged_in = True

    if not logged_in:
        return redirect("/")

    return render_template('profile.html', user=logged_in_user)


@ app.route('/forum/<int:forum_id>/posts',methods=['POST','GET'])
def get_post(forum_id):


    if request.method == 'POST':
        new_post = request.form.get('box')
        posts.create_new_post(new_post, forum_id, logged_in_user.user_id)

    post = Post.query.filter_by(forum_id=forum_id).all()#not a method call yet
    forum = Forum.query.get(forum_id) #not a method call yet
    return render_template('post.html', forum=forum, post=post)


@ app.route('/forum/<int:forum_id>/posts/create_post',methods=['POST','GET'])
def create_post(forum_id):
    
    if not logged_in:
        return redirect("/login")
    
    forum = Forum.query.get(forum_id)

    return render_template('create_post.html',forum=forum, logged_in_user=logged_in_user)


@ app.route('/forum/<int:forum_id>/posts/<int:post_id>/comments', methods=['POST','GET'])
def get_comment(forum_id,post_id):


    if request.method == 'POST':
        new_comment = request.form.get('text')
        comment.create_new_comment(new_comment, post_id, logged_in_user.user_id)


    forum = Forum.query.get(forum_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    post = Post.query.get(post_id)

    return render_template('comments.html', comments=comments, post=post, forum=forum)


@ app.route('/forum/<int:forum_id>/posts/<int:post_id>/comments/create_comment', methods=['GET','POST'])
def create_comment(forum_id,post_id):
    
    if not logged_in:
        return redirect("/login")
    
    forum = Forum.query.get(forum_id)
    post = Post.query.get(post_id)

    return render_template('create_comment.html', forum=forum, post=post)