import os
from shutil import move, rmtree
import pandas as pd
from ..generate_json.translation import subject_mapping


def walk_bids_folder(bids_path, study_path):
    """Rename all bids file with our subject id number mapping

    Expecting the same "biac_id_mapping.csv".

    params:
        - study_path: the path to the study folder
    """
    mapping = subject_mapping(study_path)
    for subj in os.listdir(bids_path):
        if subj.startswith("sub"):
            subj_date_id = subj.split("-")[1]
            subj_id = subj_date_id.split("_")[1]
            real_id = mapping.loc[int(subj_id)].Real_ID
            _renaming_all_files(os.path.join(bids_path, subj), subj_date_id, real_id)
            # rename folder, need to combine sessions
            old_name = os.path.join(bids_path, subj) 
            new_name = os.path.join(bids_path, "sub-" + real_id) 
            if os.path.exists(new_name):
                contents = os.listdir(old_name)
                for content in contents:
                    move(os.path.join(old_name, content), new_name)
                rmtree(old_name)
            else:
                os.rename(old_name, new_name)
            

def _renaming_all_files(root, subj_id, real_id):
    for subdir, _, files in os.walk(root):
        for f in files:
            if f.startswith("sub"):
                subdir_path = os.path.relpath(subdir, root)
                old_name = os.path.join(root, subdir_path, f)
                new_name = os.path.join(root, subdir_path, f.replace(subj_id, real_id))
                os.rename(old_name, new_name)


        






