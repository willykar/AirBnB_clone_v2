#!/usr/bin/python3
"""Starts a Flask web application
The web application must be listening on 0.0.0.0 port 5000
Routes:
    /:display 'Hello HBNB!"
    /hbnb: display "HBNB
    /c/<text>: display "C" followed by the value of
    the text variable
"""
from flask import Flask

app = Flask(__name__)

# index route
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"

# /hbnb route
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"

# /c/<text> route
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
