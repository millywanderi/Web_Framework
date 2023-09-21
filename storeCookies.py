#!/usr/bin/python3
"""Storing cookies"""
from flask import Flask, make_response, render_template, set_cookie


app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
