import json
import os 
from translation import trans_dict, parse_task_and_run


def build_subj(dict_to_write, subject, session):
    dict_to_write["sub"] = subject
    dict_to_write["ses"] = session


def build_funcs(dict_to_write, subject, path, trans_dict):
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


def write_to_json(dict_to_write, filepath):
    with open(filepath, "w") as f:
        json.dump(dict_to_write, f)



### Testing
d = dict()
build_subj(d, "19338", "")
build_funcs(d, "19338", "/Users/lpjiang/Research/CBT/Data/", 
    trans_dict("/Users/lpjiang/Research/CBT/Data/func/19338/series_order_note.txt"))
write_to_json(d, "./19338.json")
        
    


