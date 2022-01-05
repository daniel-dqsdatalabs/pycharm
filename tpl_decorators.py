# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=broad-except

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'


import time
from functools import wraps


def exectime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f'Ejecutado en {elapsed_time:.6f} seg.')
        return func(*args, **kwargs)
    return wrapper
