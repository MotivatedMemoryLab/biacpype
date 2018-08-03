import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biac2bids.prep.convert import run_all

### CHANGE HERE ###
# TODO: check: 19425, 19239
SUBJECTS = ['19492', '19636', '19671', '19418', '19480', '19357', '19761', '19589', '19658', '19497', '19338']
STUDY_PATH = "/Users/lpjiang/Research/CBT/"
JSON_OUTPUT_PATH = "/Users/lpjiang/Research/CBT/JSONS/" 
TRANSLATION_FILE_NAME = "series_order_note.txt" 
SESSION = ""

run_all(SUBJECTS, SESSION, STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH)
print("Done")