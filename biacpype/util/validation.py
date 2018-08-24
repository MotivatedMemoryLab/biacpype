import os
import shutil
import pandas as pd
from ..biac2bids.generate_json.translation import trans_dict


def verify_biac_path(dirpath):
    # check study path contains Data/ and valid biac_id_mapping.csv
    if not os.path.exists(dirpath):
        return "This path does not exist!"
    contents = os.listdir(dirpath)
    if "biac_id_mapping.csv" not in contents:
        return "biac_id_mapping.csv is not in this biac directory!"
    if not valid_biac_id_mapping_file(os.path.join(dirpath, "biac_id_mapping.csv")):
        return "biac_id_mapping.csv has invalid header"
    if "Data" not in contents:
        return "Folder \"Data\" is not in this biac directory!"
    # check anat and func in Data
    dirpath = os.path.join(dirpath, "Data")
    sub_contents = os.listdir(dirpath)
    if "Anat" not in sub_contents or "Func" not in sub_contents:
        return "\"Anat\" or \"Func\" or \"Behavioral\" are not the subfolders of Data"
    # verify anat and func has the same folders
    anat_folders = os.listdir(os.path.join(dirpath, "Anat")) 
    func_folders = os.listdir(os.path.join(dirpath, "Func"))  
    if anat_folders != func_folders:
        return "\"Anat\" and \"Func\" contains different folders!" 

    return None


def basic_structrue(study_path):
    # check study path contains Data/ and valid biac_id_mapping.csv
    if not os.path.exists(dirpath):
        raise OSError("The study path not found!")
    contents = os.listdir(dirpath)
    if "biac_id_mapping.csv" not in contents:
        raise ValueError("biac_id_mapping.csv is not in this biac directory!")
    if "Data" not in contents:
        raise ValueError("Folder \"Data\" is not in this biac directory!")
    # check anat and func in Data
    dirpath = os.path.join(dirpath, "Data")
    sub_contents = os.listdir(dirpath)
    if "Anat" not in sub_contents or "Func" not in sub_contents:
        raise ValueError("\"Anat\" or \"Func\" or \"Behavioral\" are not the subfolders of Data")
    # verify anat and func has the same folders
    anat_folders = os.listdir(os.path.join(dirpath, "Anat")) 
    func_folders = os.listdir(os.path.join(dirpath, "Func"))  
    if anat_folders != func_folders:
        raise ValueError("\"Anat\" and \"Func\" contains different folders!")

    
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


def valid_biac_id_mapping_file(filepath):
    with open(filepath, "r") as f:
        headers = f.readline().split(",")
        valid = True
        if len(headers) == 2:
            valid = valid and (headers[0] == "BIAC_ID") and (headers[1] == "Real_ID")
        elif len(headers) == 3:
            valid = valid and (headers[0] == "BIAC_ID") and (headers[1] == "Session") and (headers[2] == "Real_ID")
        else:
            valid = False
        return valid


def verify_data_folder(data_folder):

    pass  
    

def valid_raw_file_names(filepath):
    pass
