#!/usr/bin/python3
""" cript that starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template


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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def pytext(text='is_cool'):
    """ function returns a string Python + <text> """
    return "{} {}".format('Python', text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_even(n):
    return render_template('6-number_odd_or_even.html', number=n)



if __name__ == "__main__":
    app.run()
