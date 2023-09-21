#!/usr/bin/python3
"""Return value from a view function"""
from flask import Flask, render_template


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 # This gives a view without make response
