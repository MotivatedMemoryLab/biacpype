import os
import unittest
from biacpype.util.translation import trans_dict


class TranslationTest(unittest.TestCase):

    def test_trans(self):
        d = trans_dict("tests/files/study_folder_valid/Data/Func/19357")
        assert d["4"] == "LOCALIZER"



