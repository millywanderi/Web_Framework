#!/usr/bin/python3
"""
Escaping user-generated output to protect from injection attacks
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
