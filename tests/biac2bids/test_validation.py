import os
import unittest
from biacpype.util.validation import basic_structrue

print(os.path.join(os.path.abspath(__file__), "test/files/study_path_valid"))

class ValidationTest(unittest.TestCase):

    def test_basic_structure(self):
        basic_structrue("tests/files/study_folder_valid")