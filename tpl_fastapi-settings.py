# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=broad-except

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'

from os import path
from environs import Env
from pydantic import BaseSettings
from logger import logger

ENV_FILE = path.join(path.abspath(path.dirname(__file__)), '.env')

try:
    ENVIR = Env()
    ENVIR.read_env()
    logger.info('Configuration successfully loaded')
except Exception as e:
    print(f'Warning: .env file not found: {e}')
    logger.error(f'{e}')


class Settings(BaseSettings):
    """ This is the generic loader that sets common attributes and variables """
    # Set this out according to your development phase
    ENV: str = ENVIR('ENV', 'development')
    # Database details
    DB_TYPE: str = ENVIR('DB_TYPE', 'postgres')
    DB_HOST: str = ENVIR('DB_HOST', None)
    DB_PORT: int = ENVIR('DB_PORT', 5432)
    DB_USER: str = ENVIR('DB_USER', None)
    DB_PASS: str = ENVIR('DB_PASS', None)
    DB_DBASE: str = ENVIR('DB_DBASE', None)
    # App secret key for entropy purposes
    SECRET_KEY: str = ENVIR('SECRET_KEY', 'NoSecretKeyDefined')


settings = Settings()
