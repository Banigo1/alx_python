"""
This script starts a Flask web application that listens on
0.0.0.0, port 5000.

The option strict_slashes=False is used in all
route definitions to allow for trailing slashes in the URLs.


It has the following routes:

/: displays “Hello HBNB!”
/hbnb: displays “HBNB”
/c/<text>: displays "C ", followed by the value of the
text variable (replace underscore _ symbols with a space)
/python/(<text>): displays "Python", followed by the value of
the text variable (replace underscore _ symbols with a space).
    The default value of text is “is cool”.
/number/<n>: displays “n is a number” only if n is an integer.
/number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
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
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return '<html><body><h1>Number: {}</h1></body></html>'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return '<html><body><h1>Number: {} is {}</h1></body></html>'.format(n, result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
