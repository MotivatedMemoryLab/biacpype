import sys, os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import argparse
from biacpype.util.validation import verify_biac_path
from biacpype.util.constants import set_paths


parser = argparse.ArgumentParser(description='validation')
parser.add_argument('study_path', help='path to your study folder')

### validation begins ###
args = parser.parse_args()
set_paths(STUDY_PATH=args.study_path)
verify_biac_path()
