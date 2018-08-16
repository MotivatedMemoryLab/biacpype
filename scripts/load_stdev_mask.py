import os
import sys

### CHANGE HERE TO YOUR STUDY FOLDER ###
study_path = "/Volumes/adcock_lab/main/studies/CBT.01/"


if len(sys.argv) != 2:
    print("Usage: python load_stdev_cluster.py [subjectid]")
    exit() 

subject = sys.argv[1]

mask = study_path + "from_kelvin/" + subject + "/localizer_cluster_ROIs/" + "sphere_zstat1_mask1.hdr"
stdev_path = study_path + "/data/func/" + subject + "/imageStats/" 
stdev_maps = [stdev_path + i for i in os.listdir(stdev_path) if i.endswith("stdev.nii.gz") and i.startswith("bia5")]
os.system("fslview_deprecated " + mask + " " + " " .join(stdev_maps))




