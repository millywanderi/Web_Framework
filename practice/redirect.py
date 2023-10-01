#!/usr/bin/python3
"""Redirect a user to another endpoint"""
from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
