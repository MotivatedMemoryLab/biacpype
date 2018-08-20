import json
import os 
import re
from .translation import trans_dict, parse_task_and_run


__all__ = ['generate_all_jsons']

### call this ###
def generate_all_jsons(study_path, trans_file_name, session, output_path):
    return _walk_study_path(study_path, trans_file_name, session, output_path)
    

def _walk_study_path(study_path, trans_file_name, session, output_path):
    func_path = os.path.join(study_path, "Data", "Func") 
    func_folders = os.listdir(func_path)
    regex = re.compile('\d+_\d+')
    func_folders = filter(regex.search, func_folders)
    # dict to write to json
    dict_to_write = dict()
    # go through all subjects
    all_subjects_id = []
    for func in func_folders:
        _, subject = func.split("_")
        print(subject)
        if subject == "19239":
            continue
        all_subjects_id.append(func)
        # build trans_dict
        trans_d = trans_dict(trans_file_name, os.path.join(func_path, func))
        # build header
        _build_subj(dict_to_write, func, session)
        # build for func
        _build_contents(dict_to_write, study_path, func, trans_dict=trans_d)
        # build for anat
        # _build_contents(dict_to_write, study_path, func, trans_dict=None)
        # output
        _write_to_json(dict_to_write, output_path, func)  
    return all_subjects_id
        

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

