"""
This script implements a Flask web application that listens on
0.0.0.0, port 5000.

It has four routes:

    /, /hbnb, /c/<text>, and /python/(<text>), which display
    "Hello HBNB!", "HBNB", "C" followed by the value of the text variable
    (with underscores replaced by spaces), and "Python"
    followed by the value of the text variable
    (with underscores replaced by spaces), respectively.
    The default value of text for the /python/(<text>) route is "is cool".
    The option strict_slashes=False is used in the route definitions
    to allow for URLs with or without a trailing slash.


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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
