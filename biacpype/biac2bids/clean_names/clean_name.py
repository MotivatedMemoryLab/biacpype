import os
from shutil import move, rmtree
import biacpype.util.constants as Const
from biacpype.util.translation import subject_mapping


def group_sessions():
    """Rename all bids file with our subject id number mapping

    Expecting the same "biac_id_mapping.tsv".

    params:
        - Const.STUDY_PATH: the path to the study folder
    """
    mapping = subject_mapping(Const.STUDY_PATH)
    for subj in os.listdir(Const.BIDS_PATH):
        if subj.startswith("sub"):
            subj_date_id = subj.split("-")[1]
            subj_id = subj_date_id.split("_")[1]
            real_id = mapping.loc[int(subj_id)].Real_ID
            _renaming_all_files(os.path.join(Const.BIDS_PATH, subj), subj_date_id, real_id)
            # rename folder, need to combine sessions
            old_name = os.path.join(Const.BIDS_PATH, subj) 
            new_name = os.path.join(Const.BIDS_PATH, "sub-" + real_id) 
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


        






