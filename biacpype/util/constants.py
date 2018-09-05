import os


STUDY_PATH = None
SUBJECTS = None
JSON_OUTPUT_PATH = None
BIDS_PATH = None
LOG_PATH = None # log of bxh2bids
SYS_LOG = os.path.join(os.path.dirname(__file__), "../logs")


def set_paths(**kwargs):
    global STUDY_PATH
    global SUBJECTS
    global JSON_OUTPUT_PATH
    global BIDS_PATH
    global LOG_PATH
    
    STUDY_PATH = kwargs.get("STUDY_PATH", "")
    SUBJECTS = kwargs.get("SUBJECTS", None)
    if SUBJECTS:
        assert type(SUBJECTS) is list
    JSON_OUTPUT_PATH = kwargs.get("JSON_OUTPUT_PATH", "")
    LOG_PATH = kwargs.get("LOG_PATH", "")
    BIDS_PATH = kwargs.get("BIDS_PATH", "")
    