#!/usr/bin/python3
"""abort the request early with an error code"""
from flask import Flask, abort


app = Flask(__name__)

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
