import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.biac2bids.generate_json.convert import run_all
from biacpype.biac2bids.bxh2bids.run_bxh2bids import run
from biacpype.biac2bids.clean_names.clean_name import walk_bids_folder

### CHANGE HERE ###
STUDY_PATH = "/Volumes/lj146/Documents/CBT.01/"
JSON_OUTPUT_PATH = "/Volumes/lj146/Documents/CBT.01/JSONS-new/" 
TRANSLATION_FILE_NAME = "series_order_note.txt" 
SESSION = ""
BIDS_PATH = "/Volumes/lj146/Documents/CBT.01/bids-try/"
LOG_PATH = "/Volumes/lj146/Documents/CBT.01/logs/"

# ---------pipe begins---------  # 

# generate jsons
run_all(SESSION, STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH, BIDS_PATH, LOG_PATH)

# convert to bids
run(os.path.join(JSON_OUTPUT_PATH, "bxh2bids_hopes_dreams.json"))

# clean up
walk_bids_folder(BIDS_PATH, "/Volumes/lj146/Documents/CBT.01/biac_id_to_subject.csv")


