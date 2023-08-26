"""
This module implements a Flask web application.

The web application listens on
0.0.0.0, port 5000 and provides the following
routes:

/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable 
(replace underscore _ symbols with a space )


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

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
