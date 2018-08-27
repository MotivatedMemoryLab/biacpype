import os
import logging
from . import constants as Const


def get_logger(level, log_file, mode='a'):

    # make sure log folder exists
    if not os.path.exists(Const.SYS_LOG):
        os.mkdir(Const.SYS_LOG)

    logger = logging.getLogger(log_file)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(level)
    log_file = logging.FileHandler(os.path.join(Const.SYS_LOG, log_file), mode=mode)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_file.setFormatter(log_format)

    logger.addHandler(log_file)    
    return logger
