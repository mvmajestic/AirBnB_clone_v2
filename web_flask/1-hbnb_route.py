#!/usr/bin/python3
"""Will start a Flask Web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when route queried
    """
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
