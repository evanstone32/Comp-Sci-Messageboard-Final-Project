from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:GroupPass123@localhost:3306/Forum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/login')
def list_all_movies():
    return render_template('login.html')

@app.get('/SignUp')
def sign_up():
    return render_template('sign_up.html')

@app.get('/forum')
def forum():
    return render_template('forum.html')


@app.get('/posts')
def create_movies_form():
    return render_template('posts.html')


@app.post('/posts')
def create_movie():
    return redirect('/posts')
