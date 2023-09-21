#!/usr/bin/python3
"""make response object"""
from flask import Flask, make_response, render_template


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
