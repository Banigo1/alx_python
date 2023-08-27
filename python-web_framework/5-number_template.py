"""

This script starts a Flask web application that listens on
0.0.0.0, port 5000.

It has the following routes:

/: displays “Hello HBNB!”
/hbnb: displays “HBNB”
/c/<text>: displays "C ", followed by the value of the text variable
(replace underscore _ symbols with a space)
/python/(<text>): displays "Python ",
followed by the value of the text variable
(replace underscore _ symbols with a space).
The default value of text is “is cool”.
/number/<n>: displays “n is a number” only if n is an integer.
/number_template/<n>: displays an HTML page only if n is an integer,
with an H1 tag containing “Number: n” inside the BODY tag.
The option strict_slashes=False is used in all
route definitions to allow for trailing slashes in the URLs.

"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
