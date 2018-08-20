import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biac2bids.prep.generate_json import walk_study_path



walk_study_path("/Users/lj146/Documents/CBT.01")
