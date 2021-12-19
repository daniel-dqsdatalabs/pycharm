# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=broad-except

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'

import uvicorn
import psycopg2
from fastapi import FastAPI
from logger import logger
from settings import settings as myvar


# Application initialization
app = FastAPI(title="My API", openapi_url="/openapi.json", )


# Database connection initialization
def db_connect():
    """ PostgreSQL database connection """
    db = f'host={myvar.DB_HOST} ' \
         f'port={myvar.DB_PORT} ' \
         f'user={myvar.DB_USER} ' \
         f'pass={myvar.DB_PASS} ' \
         f'dbase={myvar.DB_DBASE}'
    c = psycopg2.connect(db)
    logger.info('Database connected successfully')
    return c


@app.get('/')
def index() -> dict:
    """ Example function with type annotations """
    return {
        'status': 'info',
        'host': myvar.DB_HOST,
        'port': myvar.DB_PORT,
        'user': myvar.DB_USER,
        'pass': myvar.DB_PASS,
        'dbase': myvar.DB_DBASE
    }


@app.get("/foo/{item_id}")
def read_item(item_id):
    """ Example function """
    return {
        'foo': item_id
    }


@app.options('/number/{item_id}')
def options(item_id: int) -> dict:
    """ Example function """
    return {
        'options': 'post'
    }


@app.post('/number/{item_id}')
def read_int_item(item_id: int) -> dict:
    """ Example function """
    return {
        'foo': item_id
    }


@app.get("/heartbeat")
async def heartbeat():
    """ Example heartbeat function for proxies and load balancers to check """
    return {
        'status': 'ok'
    }


# This is where the Python program (not the API) effectively starts
def main():
    """ Main programme """
    # noinspection PyTypeChecker
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Don't modify anything beyond this point
if __name__ == '__main__':
    main()
