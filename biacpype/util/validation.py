import os
import shutil
import logging
import pandas as pd
from .decorators import logged
from .translation import trans_dict
from .create_logger import get_logger
from . import constants as Const
from .InvalidFileError import InvalidFileError


def verify_biac_path():
    """This is the pipeline to verify the study path has everything needed to
    be automatically converted to BIDS format. The steps are:

    1. basic_structure: check folder has {Data, biac_id_mapping.tsv}, Data has {Anat, Func}, 
        both Anat and Func contain the same folders, and each of these folders contains series_order_note.tsv
    
    2. biac_id_mapping_file: check biac_id_mapping.tsv is valid

    3. all_series_order_note_files: check all series_order_note.tsv files in each subfolder is valid

    4. data_folder_file_matching: check each .bxh file is matched with .nii.gz file, and has valid task code
        translation which can be found in series_order_note.tsv 

    Logs generated during validation can be found in biacpype/logs/validation.log
    """
    logger = get_logger(logging.DEBUG, "validation.log", mode='w') # clear file if existed
    logger.info("Start validation...")
    basic_structrue(Const.STUDY_PATH)
    biac_id_mapping_file(os.path.join(Const.STUDY_PATH, "biac_id_mapping.tsv"))
    all_series_order_note_files(Const.STUDY_PATH)
    data_folder_file_matching(Const.STUDY_PATH, folder_type="Anat")
    data_folder_file_matching(Const.STUDY_PATH, folder_type="Func")
    error_lines = parse_validation_file(os.path.join(Const.SYS_LOG, "validation.log"))
    if not len(error_lines):
        print("Your study path passed validation! You are now ready for conversion")
    else:
        print("### Following erros happend: ###")
        for line in error_lines:
            print(line)


@logged("validation.log")
def data_folder_file_matching(study_path, folder_type="Func"):
    # first Func
    data_path =  os.path.join(study_path, "Data", folder_type) 
    data_folders = os.listdir(data_path)
    for folder in data_folders:
        if not folder.startswith("."):
            # check if the rest of files have valid naming
            all_files = os.listdir(os.path.join(data_path, folder)) 
            bxh_files = filter(lambda x: x.endswith(".bxh"), all_files)
            # build series_order_note dictionrary
            trans_d = trans_dict(os.path.join(data_path, folder))
            for bxh_file in bxh_files:
                # check valid file naming
                bxh_name = bxh_file.rstrip(".bxh")    
                info = bxh_name.split("_")
                if len(info) != 3 and len(info) != 4:
                    raise InvalidFileError("Invalid naming", os.path.join(data_path, folder, bxh_file))
                # check matching nii.gz file
                if bxh_name + ".nii.gz" not in all_files:
                    raise InvalidFileError("Did not find matching nii.gz file: ", os.path.join(data_path, folder, bxh_file))
                # check that the task code is in dictionary
                if info[2] not in trans_d:
                    raise InvalidFileError("task code not found in series_order_note.tsv", os.path.join(data_path, folder, bxh_file))
                

def all_series_order_note_files(study_path):
    anat_folders = os.listdir(os.path.join(study_path, "Data", "Anat")) 
    func_folders = os.listdir(os.path.join(study_path, "Data", "Func"))  
    # check all subfolders have valid series_order_note.tsv
    for folder in anat_folders:
        if not folder.startswith("."): 
            series_order_note_file(os.path.join(study_path, "Data", "Anat", folder, "series_order_note.tsv"))
    for folder in func_folders:
        if not folder.startswith("."): 
            series_order_note_file(os.path.join(study_path, "Data", "Func", folder, "series_order_note.tsv"))


@logged("validation.log")
def basic_structrue(study_path):
    # check study path contains Data/ and valid biac_id_mapping.csv
    if not os.path.exists(study_path):
        raise OSError("The study path not found!")
    contents = os.listdir(study_path)
    if "biac_id_mapping.tsv" not in contents:
        raise ValueError("biac_id_mapping.tsv is not in this biac directory!")
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
    # check all subfolders have series_order_note.tsv
    for folder in anat_folders:
        if not folder.startswith(".") and "series_order_note.tsv" not in os.listdir(os.path.join(subpath, "Anat", folder)):
            raise ValueError("{} does not contain series_order_note.tsv".format(os.path.join(subpath, "Anat", folder)))
    for folder in func_folders:
        if not folder.startswith(".") and "series_order_note.tsv" not in os.listdir(os.path.join(subpath, "Func", folder)):
            raise ValueError("{} does not contain series_order_note.tsv".format(os.path.join(subpath, "Func", folder)))
        

@logged("validation.log")
def biac_id_mapping_file(filepath):
    with open(filepath, "r") as f:
        headers = f.readline().rstrip().split("\t")
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
            raise InvalidFileError("biac_id_mapping.tsv header not valid! Please check user manual", filepath)
        # check the rest of the lines
        biac_ids = set() 
        for line_number, line in enumerate(f):
            info = line.split("\t") 
            if len(info) != num_headers:
                raise InvalidFileError("line {} is not valid: it has {} parts".format(line_number + 2, len(info)), filepath)
            if info[0] in biac_ids:
                raise InvalidFileError("line {} has duplicate biac_id: {}".format(line_number + 2, info[0]), filepath)
            biac_ids.add(info[0])                


@logged("validation.log")
def series_order_note_file(filepath):
    with open(filepath, "r") as f:
        task_code = set()
        for line_number, line in enumerate(f):
            info = line.split("\t") 
            if len(info) != 2:
                raise InvalidFileError("line {} is not valid: it has {} parts".format(line_number + 1, len(info)), filepath)
            if info[0] in task_code:
                raise InvalidFileError("line {} has duplicate task code: {}".format(line_number + 1, info[0]), filepath)
            task_code.add(info[0])                


def parse_validation_file(log_file):
    lines = None # its' just good practice
    with open(log_file, "r") as f:
        lines = []
        for i in f:
            if "ERROR" in i:
                lines.append(i) 
    return lines


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
