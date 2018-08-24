import json
import os 
import re
from .translation import trans_dict, parse_task_and_run, subject_mapping


__all__ = ['generate_all_jsons']


### call this ###
def generate_all_jsons(study_path, output_path):
    """Generate jsons for all subject and sessions

    params:
        - study_path: the path to the study folder
        - output_path: the path to output generated json files
    
    returns: 
        - a list of subjects runned
    """
    return _walk_study_path(study_path, output_path)
    

def _walk_study_path(study_path, output_path):
    func_path = os.path.join(study_path, "Data", "Func") 
    func_folders = os.listdir(func_path)
    regex = re.compile('\d+_\d+')
    func_folders = filter(regex.search, func_folders)
    # subject mapping file
    mapping = subject_mapping(study_path)
    session = None
    if "Session" not in mapping.columns:
        session = ""
    # dict to write to json
    dict_to_write = dict()
    # go through all subjects
    all_subjects_id = []
    for func in func_folders:
        _, subject = func.split("_")
        if subject == "19239":
            continue
        all_subjects_id.append(func)
        # build trans_dict
        trans_d = trans_dict(os.path.join(func_path, func))
        # build header
        if session != "":
            session = mapping.loc[int(subject)].Session
        _build_subj(dict_to_write, func, session)
        # build for func
        _build_contents(dict_to_write, study_path, func, trans_d, True)
        # build for anat
        _build_contents(dict_to_write, study_path, func, trans_d, False)
        # output
        _write_to_json(dict_to_write, output_path, func)  
    return all_subjects_id
        

def _build_subj(dict_to_write, subject, session):
    dict_to_write["sub"] = subject
    dict_to_write["ses"] = session


def _build_contents(dict_to_write, study_path, subject, trans_dict, func):
    if func:
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
            if func:
                content["task"] = task_name
            else:
                content["acq"] = task_name
            content["run"]  = run
            contents[json_field] = content
    key = "funcs" if func else "anats"
    dict_to_write[key] = contents


def _write_to_json(dict_to_write, output_path, subject):
    with open(output_path + subject + ".json", "w") as f:
        json.dump(dict_to_write, f)

