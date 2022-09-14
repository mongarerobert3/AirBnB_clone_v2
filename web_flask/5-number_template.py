#!/usr/bin/python3
"""script that starts a Flask web application
/hbnb: display “HBNB””"""


from flask import Flask, render_template
from sys import argv

# Instanciating flask on app
app = Flask(__name__)


# Routes and decorator
@app.route('/', strict_slashes=False)
def homepage():
    """display “Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C <text>"""
    text = text.replace('_', ' ')
    return ("C " + text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display Python <text>"""
    text = text.replace('_', ' ')
    return ("Python " + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


# Running flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
