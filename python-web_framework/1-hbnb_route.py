"""
This script creates a Flask web application that listens on 0.0.0.0, port 5000.

It has two routes:

    / and /hbnb, which display
    "Hello HBNB!" and "HBNB", respectively.

The option strict_slashes=False is used in the
route definitions to allow for URLs with or without a trailing slash.

Usage:

    To start the web application,
    run this module directly.

"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
