#!/usr/bin/python3
"""
    script that starts a Flask web application:
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display C <text>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display Python <text>"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """display <n> is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display HTML page with h1-> Number: n """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
