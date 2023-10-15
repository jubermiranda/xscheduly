"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import unittest
import os
import sys

sys.path.append(os.path.abspath('../../src'))

TEST_FILE_PATH = "templates/table_test.odt"
STD_COLUM_NUMBER = 2

from src.xscheduly_manager.odt_table_extractor import OdtTableExtractor

class TestOdtTableExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = OdtTableExtractor()

    def test_file_has_table(self):
        self.assertTrue(self.extractor.check_content_format())

if __name__ == '__main__':
    unittest.main()
