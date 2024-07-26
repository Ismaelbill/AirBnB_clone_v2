#!/usr/bin/python3
""" cript that starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=True)
def hello_hbnb():
    """ function returns a string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=True)
def hbnb():
    """ function returns a string """
    return "HBNB"


if __name__ == "__main__":
    app.run()
