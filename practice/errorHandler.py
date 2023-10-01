#!/usr/bin/python3
"""Customize error page using errorhandler"""
from flask import Flask, render_template


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
