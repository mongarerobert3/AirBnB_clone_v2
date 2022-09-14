#!/usr/bin/python3
"""script that starts a Flask web application
and display “Hello HBNB!”"""


from flask import Flask

# Instanciating flask on app
app = Flask(__name__)


# Route and decorator
@app.route('/', strict_slashes=False)
def home():
    """display “Hello HBNB!"""
    return("Hello HBNB!")


# Running flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
