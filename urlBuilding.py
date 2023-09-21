#!/usr/bin/python3
"""url_for() to build a specific function"""

from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Hannah Joy'))

"""
OUTPUT
/
/login
/login?next=/
/user/Hannah%20Joy
"""
