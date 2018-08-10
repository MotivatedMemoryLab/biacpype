import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biac2bids.prep.convert import run_all

### CHANGE HERE ###
# TODO: check: 19425, 19239
<<<<<<< HEAD
SUBJECTS = ['19492', '19239', '19636', '19671', '19418', '19480', '19357', '19761', '19589', '19658', '19497', '19425', '19338']
STUDY_PATH = "/Users/lpjiang/Research/CBT/"
JSON_OUTPUT_PATH = "/Users/lpjiang/Research/CBT/JSONS/" 
=======
SUBJECTS = ['19239', '19338', '19357', '19418', '19425', '19480', '19492', '19497', '19589', '19636', '19658', '19671', '19761'] 
STUDY_PATH = "/Users/lj146/Documents/CBT/"
JSON_OUTPUT_PATH = "/Users/lj146/Documents/CBT/JSONS/" 
>>>>>>> b2b1d41d0a4d531e403ce958f18c114ca28d1ace
TRANSLATION_FILE_NAME = "series_order_note.txt" 
SESSION = ""
BIDS_PATH = "/Users/lj146/Documents/CBT/bids-try/"
LOG_PATH = "/Users/lj146/Documents/CBT/bids-try/logs/"


run_all(SUBJECTS, SESSION, STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH, BIDS_PATH, LOG_PATH)
print("Done")