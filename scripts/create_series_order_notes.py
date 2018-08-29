import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.util.constants import set_paths
from biacpype.helper.create_series_order_note import populate_file


STUDY_PATH = "/Volumes/lj146/Documents/CBT.01/"
# translation dictionary
anat_d = {
    "001": "fmap", 
    "003": "Anat",
    "005": "Anat",
}

func_d = {
    "4": "LOCALIZER", 
    "5": "TRAIN",
    "6": "REST",
    "7": "FINISH" 
}
subjs = ["20150220_19480"] # or None for all subjects

### creation begins ###
set_paths(STUDY_PATH=STUDY_PATH)
populate_file("Anat", anat_d, subjs=subjs)
populate_file("Func", func_d, subjs=subjs)

