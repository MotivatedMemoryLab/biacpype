import os
import pandas as pd


def renaming_all_files(root, subj_id, real_id):
    for subdir, dirs, files in os.walk(root):
        for f in files:
            if f.startswith("sub"):
                subdir_path = os.path.relpath(subdir, root)
                old_name = os.path.join(root, subdir_path, f)
                new_name = os.path.join(root, subdir_path, f.replace(subj_id, real_id))
                os.rename(old_name, new_name)

bids_data_path = "/Volumes/lj146/Documents/CBT.01/bids-try/" 
csv_path = "/Volumes/lj146/Documents/CBT.01/biac_id_to_subject.csv"

df = pd.read_csv(csv_path, dtype={"Subject":str, "id":str}, index_col=None)

for subj in os.listdir(bids_data_path):
    if subj.startswith("sub"):
        subj_date_id = subj.split("-")[1]
        subj_id = subj_date_id.split("_")[1]
        real_id = df[df.Subject == subj_id].id.values[0]
        renaming_all_files(os.path.join(bids_data_path, subj), subj_date_id, real_id)
        # rename folder 
        os.rename(os.path.join(bids_data_path, subj), os.path.join(bids_data_path, "sub-" + real_id))
        






