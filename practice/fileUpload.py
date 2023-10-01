#!/usr/bin/python3
"""
Handle uploade files with Flask
Remember to set enctype="multipart/form-data" attribute on your HTML
"""
from flask import Flask, request


app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
