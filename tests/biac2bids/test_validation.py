import os
import unittest
from biacpype.util.constants import set_paths
from biacpype.util.validation import basic_structrue

print(os.path.join(os.path.abspath(__file__), "test/files/study_path_valid"))

class ValidationTest(unittest.TestCase):

    def setUp(self):
        set_paths(STUDY_PATH="test/files/study_folder_valid", JSON_OUTPUT_PATH="test/files/study_folder_valid/JSONS",
                  BIDS_PATH="test/files/study_folder_valid/bids-try", LOG_PATH="test/files/study_folder_valid/logs") 

    def test_basic_structure(self):
        basic_structrue("tests/files/study_folder_valid")