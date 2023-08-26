"""
This script creates a Flask web application that listens on
0.0.0.0, port 5000.
It has five routes:
/, /hbnb, /c/<text>, /python/(<text>), and /number/<n>, which display
"Hello HBNB!", "HBNB", "C" followed by the value of the text variable
(with underscores replaced by spaces), "Python" followed by the value of the text variable
(with underscores replaced by spaces), and "n is a number" if n is an integer, respectively.
The default value of text for the /python/(<text>) route is "is cool".
The option strict_slashes=False is used in the 
route definitions to allow for URLs with or without a trailing slash.

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

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return '%d is a number' % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
