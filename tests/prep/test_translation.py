import os
import unittest
from biacpype.biac2bids.generate_json.translation import trans_dict

class TranslationTest(unittest.TestCase):

    def test_trans(self):
        d = trans_dict("notes.txt",  "tests/files/func/100")
        assert d["4"] == "LOCALIZER"



