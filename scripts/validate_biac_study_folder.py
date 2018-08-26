import sys, os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.util.validation import verify_biac_path
from biacpype.util.create_logger import get_logger


if __name__ == "__main__":  
    logger = get_logger(logging.DEBUG, "validation.log")
    logger.info("start validation...")
    verify_biac_path("/Volumes/lj146/Documents/CBT.01/")


