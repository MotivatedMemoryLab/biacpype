import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biac2bids.prep.convert import run_all

### CHANGE HERE ###
SUBJECTS = ["19338", "19492", "19497", "19589", "19671"]
STUDY_PATH = "/Users/lpjiang/Research/CBT/"
JSON_OUTPUT_PATH = "/Users/lpjiang/Research/CBT/JSONS/" 
TRANSLATION_FILE_NAME = "series_order_note.txt" 

run_all(SUBJECTS, "", STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH)
