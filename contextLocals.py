#!/usr/bin/python3
"""
creating a request object yourself and binding it to the context.
"""
from flask import Flask, request


app = Flask(__name__)

def hello():
    with app.request_context('/hello', method='POST'):
        # do something with request until the block end
        assert request.path == '/hello'
        assert request.method == 'POST'

        # possibility is passing a whole WSGI environment to the request_context() method
        with app.request_content(environ):
            assert request.method == 'POST'
