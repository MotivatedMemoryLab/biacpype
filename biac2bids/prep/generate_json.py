import json
import os 
from translation import trans_dict, parse_task_and_run


def _build_subj(dict_to_write, subject, session):
    dict_to_write["sub"] = subject
    dict_to_write["ses"] = session


def _build_funcs(dict_to_write, subject, path, trans_dict):
    path = path + "func/" + subject  
    funcs = dict()
    for bxh_file in os.listdir(path):
        if bxh_file.endswith(".bxh"):
            func = dict()
            task_name, run, json_field = parse_task_and_run(bxh_file, trans_dict)
            # do a check and raise error here
            func["task"] = task_name
            func["run"]  = run
            funcs[json_field] = func
    dict_to_write["funcs"] = funcs


def _build_anat(dict_to_write):
    # right now, we expect to find the file "005"
    dict_to_write["anats"] = {"005": {"acq": "anat"}}


def _write_to_json(dict_to_write, output_path):
    with open(output_path, "w") as f:
        json.dump(dict_to_write, f)


def generate_json(subject, session, data_path, trans_dict, output_path):
    d = dict()
    _build_subj(d, subject, session)
    _build_funcs(d, subject, data_path, trans_dict)
    _build_anat(d)
    _write_to_json(d, output_path)
