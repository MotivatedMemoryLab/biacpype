import os
import shutil


def verify_data_dir(dirpath):
    if not os.path.exists(dirpath):
        return "This path does not exist!"
    contents = os.listdir(dirpath)
    if "Data" not in contents:
        return "Data is not a folder in this path!"
    # check anat and func in Data
    dirpath = os.path.join(dirpath, "Data")
    sub_contents = os.listdir(dirpath)
    if "anat" not in sub_contents or "func" not in sub_contents or "behavioral" not in sub_contents:
        return "anat or func or behavioral are not the subfolders of Data"
    # verify anat and func has the same folders
    anat_folders = os.listdir(os.path.join(dirpath, "anat")) 
    func_folders = os.listdir(os.path.join(dirpath, "func"))  
    return None if anat_folders == func_folders else "anat and func contains different folders!"
    

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
