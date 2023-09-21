#!/usr/bin/python3
"""
Rules for redirection Behavior
"""
from flask import Flask


app = Flask(__name__)

"""
If user enters /projects, Flask redirects the user to /projects/ 
"""
@app.route('/projects/') 
def projects():
    return 'The project page'

"""
If user inserts /about/, Flask redirects the user to 404 "Not Found"
"""
@app.route('/about')
def about():
    return 'The about page'
