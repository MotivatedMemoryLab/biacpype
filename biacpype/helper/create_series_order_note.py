import os
from ..util import constants as Const


def populate_file(folder, dictionary, subjs=None):
    assert folder == "Func" or folder == "Anat", "folder has to be 'Anat' or 'Func'"
    folder_path = os.path.join(Const.STUDY_PATH, "Data", folder)
    for folder in os.listdir(folder_path):
        if not folder.startswith(".") and include_subj(folder, subjs):
            build_file(dictionary, os.path.join(folder_path, folder, "series_order_note.tsv"))


def include_subj(subj, subjs):
    if not subjs:
        return True
    return subj in subjs


def build_file(dictionary, filepath):
    with open(filepath, "w") as f:
        for key, val in dictionary.items():
            s = key + "\t" + val
            f.write(s + "\n")

