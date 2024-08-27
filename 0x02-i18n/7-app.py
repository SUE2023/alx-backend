#!/usr/bin/env python3
""" Flask App with internationalization support."""

from flask import Flask, render_template, g, request
from flask_babel import Babel
from typing import Union, Dict
import pytz


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id."""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Register functions that will run before every request of  application.
    Checking user authentication.
    Initializing or modifying request data.
    Setting up global variables that might be needed in the view functions.
    Logging or tracking requests.
    Modifying request headers or other request attributes.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with the supported languages
    based on the following order of priority:
    1. Locale from URL parameters.
    2. Locale from user settings.
    3. Locale from request headers.
    4. Default locale.
    """
    # 1. Locale from URL parameters
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table and query_table['locale'] in \
            app.config["LANGUAGES"]:
        return query_table['locale']

    # 2. Locale from user settings
    if hasattr(g, 'user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGE'])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the timezone for a web page."""
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """Home Page """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
