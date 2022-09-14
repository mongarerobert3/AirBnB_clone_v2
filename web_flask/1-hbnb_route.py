#!/usr/bin/python3
"""script that starts a Flask web application
/hbnb: display “HBNB””"""


from flask import Flask

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


# Running flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
