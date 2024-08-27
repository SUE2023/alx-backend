#!/usr/bin/env python3
""" Flask App module"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False  # Reduce 404 with / on route


@app.route('/')
def index() -> str:
    """Home Page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
