import logging

def init_logger(level):
    logger = logging.getLogger()
    logger.setLevel(level)

    log_file = logging.FileHandler("testing.log")
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_file.setFormatter(log_format)

    logger.addHandler(log_file)    
    return logger


logger = init_logger(logging.DEBUG)

