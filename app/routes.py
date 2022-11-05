from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'milton'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'A beautiful day!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'What A beautiful day!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)