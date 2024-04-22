#!/usr/bin/python3
"""Starts a Flask web application.

The application must be listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask, render_template

app = Flask(__name__)

# index route
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"

# /hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

# /c/<text>
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python " + text

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n is a number only if n is a number"""
    return f"{n} is a number"

# /number_template
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
