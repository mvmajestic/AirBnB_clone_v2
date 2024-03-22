#!/usr/bin/python3
"""Will start Flask Web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template for request
    """
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render template based on conditional
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
