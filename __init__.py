# backend/__init__.py

from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Add other routes and logic as needed
