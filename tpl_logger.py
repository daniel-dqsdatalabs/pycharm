# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=wrong-spelling-in-comment
# pylint: disable=W0703

""" ${PROJECT_NAME} """

__author__ = '${USER}'
__date__ = '${DATE}-${TIME}'


import logging

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = logging.StreamHandler()
file_handler = logging.FileHandler("debug.log")

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# the formatter determines what our logs will look like
fmt_shell = '%(levelname)s %(asctime)s %(message)s'
fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# here we hook everything together
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)

# Log statements in your code:
# - logger.debug('this is a debug statement')
# - logger.info('this is a info statement')
# - logger.warning('this is a warning statement')
# - logger.critical('this is a critical statement')
# - logger.error('this is a error statement')
#
# Logger also accpets modifiers for extra information in logs (traceback):
# - logger.error("Error happened!", exc_info=True)
