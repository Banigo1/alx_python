"""
This module implements a Flask web application.

The web application listens on
0.0.0.0, port 5000 and provides the following
routes:
- /: Displays "Hello HBNB!"
    /hbnb: display “HBNB”

Usage:
    To start the web application,
    run this module directly:
        $ python app.py

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
