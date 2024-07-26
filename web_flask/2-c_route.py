#!/usr/bin/python3
""" cript that starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ function returns a string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ function returns a string """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """ function returns a string C + <text> """
    return "{} {}".format('C', text.replace('_', ' '))


if __name__ == "__main__":
    app.run()
