import os
import shutil
import pandas as pd
from .decorators import logged


def verify_biac_path(study_path):
    basic_structrue(study_path)
    biac_id_mapping_file(os.path.join(study_path, "biac_id_mapping.csv"))
    return None


@logged("validation.log")
def basic_structrue(study_path):
    # check study path contains Data/ and valid biac_id_mapping.csv
    if not os.path.exists(study_path):
        raise OSError("The study path not found!")
    contents = os.listdir(study_path)
    if "biac_id_mapping.csv" not in contents:
        raise ValueError("biac_id_mapping.csv is not in this biac directory!")
    if "Data" not in contents:
        raise ValueError("Folder \"Data\" is not in this biac directory!")
    # check anat and func in Data
    subpath = os.path.join(study_path, "Data")
    sub_contents = os.listdir(subpath)
    if "Anat" not in sub_contents or "Func" not in sub_contents:
        raise ValueError("\"Anat\" or \"Func\" or \"Behavioral\" are not the subfolders of Data")
    # verify anat and func has the same folders
    anat_folders = os.listdir(os.path.join(subpath, "Anat")) 
    func_folders = os.listdir(os.path.join(subpath, "Func"))  
    if anat_folders != func_folders:
        raise ValueError("\"Anat\" and \"Func\" contains different folders!")
     

@logged("validation.log")
def biac_id_mapping_file(filepath):
    with open(filepath, "r") as f:
        headers = f.readline().split(",")
        valid = True
        num_headers = 0
        if len(headers) == 2:
            valid = valid and (headers[0] == "BIAC_ID") and (headers[1] == "Real_ID")
            num_headers = 2
        elif len(headers) == 3:
            valid = valid and (headers[0] == "BIAC_ID") and (headers[1] == "Session") and (headers[2] == "Real_ID")
            num_headers = 3
        else:
            valid = False
        if not valid:
            raise ValueError("biac_id_mapping.tsv header not valid! Please check user manual")
        # check the rest of the lines
        biac_ids = set() 
        for line_number, line in enumerate(f):
            info = line.split("\t") 
            if len(info) != num_headers:
                raise ValueError("line {} is not valid: it has {} parts".format(line_number + 2, len(info)))
            if info[0] in biac_ids:
                raise ValueError("line {} has duplicate biac_id: {}".format(line_number + 2, info[0]))
            biac_ids.add(info[0])                

    
@logged("validation.log")
def data_folder(filepath):
    pass

def choose_json_dir(dirpath):
    if os.path.exists(dirpath):
        print("The output path already exists: do you want to overwrite it? [yes/no]")
        choice = input("Enter your decision: ") 
        if choice == "yes":
            shutil.rmtree(dirpath)
        else: 
            return False
    os.makedirs(dirpath)
    return True
