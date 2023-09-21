#!/usr/bin/python3
"""configuring html using in Flask"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

"""
Flask checks for templates on module or package

MODULE:
/application.py
/templates
    /hello.html

PACKAGE:
/application
    /__init__.py
    /templates
        /hello.html
"""
