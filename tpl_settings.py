# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=W0703

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'


from os import path
from environs import Env


ENV_FILE = path.join(path.abspath(path.dirname(__file__)), '.env')

try:
    ENVIR = Env()
    ENVIR.read_env()
except Exception as e:
    print(f'Warning: .env file not found: {e}')


class Config:
    """ This is the generic loader that sets common attributes and variables """
    JSON_SORT_KEYS = False
    # Set this out according to your development phase
    ENV = ENVIR('ENV', 'development')
    DEBUG = ENVIR.bool('DEBUG', False)
    TESTING = ENVIR.bool('TESTING', False)
    # Database details
    DB_TYPE = ENVIR('DB_TYPE', 'postgres')
    DB_HOST = ENVIR('DB_HOST', None)
    DB_PORT = ENVIR('DB_PORT', 5432)
    DB_USER = ENVIR('DB_USER', None)
    DB_PASS = ENVIR('DB_PASS', None)
    DB_DBASE = ENVIR('DB_DBASE', None)
    # App secret key for entropy purposes
    SECRET_KEY = ENVIR('SECRET_KEY', 'NoSecretKeyDefined')
