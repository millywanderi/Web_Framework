#!/usr/bin/python3
"""
Simple Python application using the Flask web framework to
create a web server that responds to HTTP requests.
"""
from flask import Flask

app = Flask(__name__) # creates an instance of Flask application


@app.route("/") # Tells flask which url to trigger the function
def hello_world():
    return "<p>Hello, World!</p>" # Returns the view on user's browser
