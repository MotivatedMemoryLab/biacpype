import unittest
from biac2bids.prep.translation import trans_dict

class TranslationTest(unittest.TestCase):

    def test_trans(self):
        d = trans_dict("tests/files/notes.txt")
        assert d["4"] == "LOCALIZER"



