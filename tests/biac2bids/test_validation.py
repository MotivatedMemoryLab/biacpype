import os
import unittest
from biacpype.util.constants import set_paths
from biacpype.util.validation import verify_biac_path
import biacpype.util.constants as Const


class ValidationTest(unittest.TestCase):

    def setUp(self):
        set_paths(STUDY_PATH="tests/files/study_folder_valid", JSON_OUTPUT_PATH="tests/files/study_folder_valid/JSONS",
                  BIDS_PATH="tests/files/study_folder_valid/bids-try", LOG_PATH="tests/files/study_folder_valid/logs") 

    def test_basic_structure(self):
        verify_biac_path(Const.STUDY_PATH)