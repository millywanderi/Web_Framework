#!/usr/bin/python
"""Application entry point"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

task = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/vi.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
