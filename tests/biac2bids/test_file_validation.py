import unittest
from biacpype.util.validation import biac_id_mapping_file, series_order_note_file


class BiacIdMappingValidationTest(unittest.TestCase):

    def test_wrong_num_headers(self):
        self.assertRaises(ValueError, biac_id_mapping_file("tests/files/validations/id_invalid_header_number.tsv"))        

    def test_wrong_headers_two(self):
        self.assertRaises(ValueError, biac_id_mapping_file("tests/files/validations/id_invalid_headers_two.tsv"))
        self.assertRaises(ValueError, biac_id_mapping_file("tests/files/validations/id_invalid_headers_three.tsv"))

    def test_extra_content(self):
        self.assertRaises(ValueError, biac_id_mapping_file("tests/files/validations/id_invalid_headers_extra.tsv"))

    def test_duplicate_id(self):
        self.assertRaises(ValueError, biac_id_mapping_file("tests/files/validations/id_invalid_headers_duplicate.tsv"))

    def test_valid(self):
        biac_id_mapping_file("tests/files/validations/id_valid.tsv")


class SeriesOrderNoteValidationTest(unittest.TestCase):

    def test_extra_content(self):
        self.assertRaises(ValueError, series_order_note_file("tests/files/validations/series_order_extra.tsv"))

    def test_duplicate_task(self):
        self.assertRaises(ValueError, series_order_note_file("tests/files/validations/series_order_duplicate.tsv"))
        
    def test_valid(self):
        series_order_note_file("tests/files/validations/series_order_valid.tsv")