#!/usr/bin/python3
"""read cookies using cookies attribute"""
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing
