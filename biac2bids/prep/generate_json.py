import json
import os 
from .translation import trans_dict, parse_task_and_run
import re


def _walk_study_path(dict_to_write, study_path, trans_dict):
    func_path = os.path.join(study_path, "Data", "Func") 
    func_folders = os.listdir(func_path)
    regex = re.compile('\d+_\d+')
    func_folders = filter(regex.search, func_folders)
    for func in func_folders:
        date, subj = func.split("_")
        # build for func
        _build_contents(dict_to_write, study_path, func, trans_dict=trans_dict)
        # build for anat
        _build_contents(dict_to_write, study_path, func, trans_dict=None)


def _build_subj(dict_to_write, subject, session):
    dict_to_write["sub"] = subject
    dict_to_write["ses"] = session


def _build_contents(dict_to_write, study_path, subject, trans_dict=None):
    if trans_dict:
        folder = "Func" # only Func needs translation
    else:
        folder = "Anat"
    path = os.path.join(study_path, "Data", folder, subject)
    contents = dict()
    for bxh_file in os.listdir(path):
        if bxh_file.endswith(".bxh"):
            content = dict()
            task_name, run, json_field = parse_task_and_run(bxh_file, trans_dict=trans_dict)
            # do a check and raise error here
            if trans_dict:
                content["task"] = task_name
                content["run"]  = run
                contents[json_field] = content
            else:
                content["acq"] = "anat"
                content["run"]  = run
                contents[json_field.split("_")[0]] = content
    key = "funcs" if trans_dict else "anats"
    dict_to_write[key] = contents


def _write_to_json(dict_to_write, output_path, subject):
    with open(output_path + subject + ".json", "w") as f:
        json.dump(dict_to_write, f)


def generate_json(subject, session, study_path, trans_dict, output_path):
    d = dict()
    _build_subj(d, subject, session)
    _walk_study_path(d, study_path, trans_dict)    
    _write_to_json(d, output_path, subject)

