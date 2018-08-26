import os
import logging
from .create_logger import get_logger 
from .InvalidFileError import InvalidFileError
from . import constants as Const

def logged(log_file):
    def decorate(func):
        logger = get_logger(logging.DEBUG, os.path.join(Const.SYS_LOG, log_file))
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                logger.info(func.__name__ + " OK!")
                return
            except InvalidFileError as e:
                logger.error(func.__name__ + " " + str(e.msg) + " -->" + e.filename)
        return wrapper
    return decorate

