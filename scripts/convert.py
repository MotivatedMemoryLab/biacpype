import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biac2bids.prep.convert import run_all

### CHANGE HERE ###
STUDY_PATH = "/Volumes/lj146/Documents/CBT.01/"
JSON_OUTPUT_PATH = "/Volumes/lj146/Documents/CBT.01/JSONS/" 

TRANSLATION_FILE_NAME = "series_order_note.txt" 
SESSION = ""
BIDS_PATH = "/Volumes/lj146/Documents/CBT.01/bids-try/"
LOG_PATH = "/Volumes/lj146/Documents/CBT.01/bids-try/logs/"

run_all(SESSION, STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH, BIDS_PATH, LOG_PATH)
print("Done")
