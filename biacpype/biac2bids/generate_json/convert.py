import os
import json
from .generate_json import generate_all_jsons
import biacpype.util.constants as Const 
from biacpype.util.validation import choose_json_dir


def generate_all_json_files():
    """Generate all json files needed by bxh2bids

    params:
        - study_path: path to the study folder
        - trans_file: the file name for translation (not the path)
        - json_path: path to save generated jsons
        - bids_path: path the output bids format data
        - log_path: path to save the logs
    """
    # check if the json output path is used
    if not choose_json_dir(Const.JSON_OUTPUT_PATH):
        print("Please rerun the script with a different json output path!")
        return
    # individual
    subjects = generate_all_jsons(Const.STUDY_PATH, Const.JSON_OUTPUT_PATH)
    # group
    _run_dream(Const.STUDY_PATH, Const.JSON_OUTPUT_PATH, Const.BIDS_PATH, Const.LOG_PATH, subjects)


def _run_dream(study_path, json_path, bids_path, log_path, subjects):
    d = dict()
    d["source_study_dir"] = study_path
    d["target_study_dir"] = bids_path
    d["log_dir"] = log_path
    d["ses_info_dir"] = json_path
    subj_dict = dict() 
    for subject in subjects:
        subj_dict[subject] = subject + ".json"
    d["ses_files"] = subj_dict
    with open(os.path.join(json_path, "bxh2bids_hopes_dreams.json"), "w") as f:
        json.dump(d, f)
