import logging

def init_logger(level, log_path):
    logger = logging.getLogger()
    logger.setLevel(level)

    log_file = logging.FileHandler(log_path)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_file.setFormatter(log_format)

    logger.addHandler(log_file)    
    return logger

