# Run this script to test whether Flask is running on this device properly

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'