from biac2bids.prep.translation import trans_dict

def test_trans():
    d = trans_dict("tests/files/notes.txt")
    assert d["4"] == "LOCALIZER"