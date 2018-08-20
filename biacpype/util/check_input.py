import os
import shutil


def verify_biac_path(dirpath):
    if not os.path.exists(dirpath):
        return "This path does not exist!"
    contents = os.listdir(dirpath)
    if "Data" not in contents:
        return "Folder \"Data\" is not in this biac directory!"
    # check anat and func in Data
    dirpath = os.path.join(dirpath, "Data")
    sub_contents = os.listdir(dirpath)
    if "Anat" not in sub_contents or "Func" not in sub_contents or "Behavioral" not in sub_contents:
        return "\"Anat\" or \"Func\" or \"Behavioral\" are not the subfolders of Data"
    # verify anat and func has the same folders
    anat_folders = os.listdir(os.path.join(dirpath, "Anat")) 
    func_folders = os.listdir(os.path.join(dirpath, "Func"))  
    return None if anat_folders == func_folders else "\"Anat\" and \"Func\" contains different folders!"
    

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
