import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    # NEVER HAVE DEBUG=TRUE IN PRODUCTION OR WHEN SUBMITTING!!!
    app.run(debug=True)
