import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.biac2bids.generate_json.convert import generate_all_json_files
from biacpype.biac2bids.bxh2bids.run_bxh2bids import bxh_to_bids
from biacpype.biac2bids.clean_names.clean_name import group_sessions

### CHANGE HERE ###
STUDY_PATH = "/Volumes/lj146/Documents/CBT.01/"
JSON_OUTPUT_PATH = "/Volumes/lj146/Documents/CBT.01/JSONS/" 
TRANSLATION_FILE_NAME = "series_order_note.txt" 
BIDS_PATH = "/Volumes/lj146/Documents/CBT.01/bids-try/"
LOG_PATH = "/Volumes/lj146/Documents/CBT.01/logs/"

# ---------pipe begins---------  # 

# generate jsons
generate_all_json_files(STUDY_PATH, TRANSLATION_FILE_NAME, JSON_OUTPUT_PATH, BIDS_PATH, LOG_PATH)

# convert to bids
bxh_to_bids(os.path.join(JSON_OUTPUT_PATH, "bxh2bids_hopes_dreams.json"))

# clean up
group_sessions(BIDS_PATH, "/Volumes/lj146/Documents/CBT.01")


