#!/usr/bin/env python3
""" Flask App with internationalization support."""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Language configuration, keeps track of supported languages list"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_pyfile('mysettings.cfg')
app.url_map.strict_slashes = False  # Reduce 404 with / on route
babel = Babel(app, locale_selector=get_locale)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with the supported languages hence
    retrieves the locale for a web page
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Home Page """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
