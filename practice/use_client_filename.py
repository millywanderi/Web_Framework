#!/usr/bin/python3
"""
Use the file name used by client before sending the file in server
NB/ use secure_filename() function
"""
from flask import Flask, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f'/var/www/uploads/{secure_filename(file.filename)}'
