import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import argparse
from biacpype.biac2bids.generate_json.convert import generate_all_json_files
from biacpype.biac2bids.bxh2bids.run_bxh2bids import bxh_to_bids
from biacpype.biac2bids.clean_names.clean_name import group_sessions
from biacpype.util.constants import set_paths



parser = argparse.ArgumentParser(description='validation')
parser.add_argument('study_path', help='path to your study folder')
parser.add_argument('json_path', help='path to output json files')
parser.add_argument('bids_path', help='path to output BIDS data')
parser.add_argument('log_path', help='path to output logs')
parser.add_argument('--subjects', help='list of subjects', nargs='*')

# ---------pipe begins---------  # 
args = parser.parse_args()
print(args.subjects)
# set paths
set_paths(STUDY_PATH=args.study_path, JSON_OUTPUT_PATH=args.json_path, BIDS_PATH=args.bids_path, LOG_PATH=args.log_path, SUBJECTS=args.subjects)
# generate jsons
generate_all_json_files()
# convert to bids
bxh_to_bids()
# clean up
group_sessions()
