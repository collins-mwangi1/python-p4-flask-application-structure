#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# append to server/app.py

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/profile/<username>')
def profile(username):
    return f'<h1>Profile for {username}</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

