# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=W0703

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'


from datetime import datetime
from flask import Flask, make_response, url_for, request
from cerberus import Validator
from logger import logger
import psycopg2
import settings


# Application initialization
APP = Flask('${PROJECT_NAME}')
APP.config.from_object(getattr(settings, 'Config'))


# Incoming data validation with Cerberus
schema_xxxxxxx = {
    'xxxxxxx': {'type': 'string', 'empty': False}
}


# Database connection initialization
def db_connect():
    """ PostgreSQL database connection """
    db = f'host={settings.Config.DB_HOST} ' \
         f'port={settings.Config.DB_PORT} ' \
         f'user={settings.Config.DB_USER} ' \
         f'pass={settings.Config.DB_PASS} ' \
         f'dbase={settings.Config.DB_DBASE}'
    c = psycopg2.connect(db)
    return c


# This functions control how to respond to common errors
@APP.errorhandler(404)
def not_found(error):
    """ HTTP Error 404 Not Found """
    data = {
        'error': 'true',
        'msg': str(error),
        'base_url': url_for('index', _external=True)
    }
    headers = {}
    return make_response(data, 404, headers)


@APP.errorhandler(405)
def not_allowed(error):
    """ HTTP Error 405 Not Allowed """
    data = {
        'error': 'true',
        'msg': str(error),
        'base_url': url_for('index', _external=True)
    }
    headers = {}
    return make_response(data, 405, headers)


@APP.errorhandler(500)
def internal_error(error):
    """ HTTP Error 500 Internal Server Error """
    data = {
        'error': 'true',
        'msg': str(error),
        'base_url': url_for('index', _external=True)
    }
    headers = {}
    return make_response(data, 500, headers)


# This piece of code controls what happens during the HTTP transaction
@APP.before_request
def before_request():
    """ This function handles HTTP request as it arrives to the API """
    pass


@APP.after_request
def after_request(response):
    """ This function handles HTTP response before send it back to client  """
    return response


# This is where the API effectively starts
@APP.route('/', methods=['GET'])
def index():
    """ This is the main function of the `/` (apex) endpoint """

    # Put now your code here

    data = {
        'tstamp': datetime.utcnow().isoformat()+'Z',
        'url_base': url_for('index', _external=True)
    }

    headers = {}
    return make_response(data, 200, headers)


# This is where the Python program (not the API) effectively starts
def main():
    """ Main programme """

    # Put now your code here

    APP.run(host='0.0.0.0', port=5000)


# Don't modify anything beyond this point
if __name__ == '__main__':
    main()
