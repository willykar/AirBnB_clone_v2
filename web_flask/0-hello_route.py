#!/usr/bin/python3
"""
A script that starts a Flask web application:
    The web application must be listening on 0.0.0.0 port 5000
    Routes:
    display "Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


# index route
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
