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

    def test_get_tables_from_odt_file(self):
        self.assertTrue(len( self.extractor.get_tables_from_odt_file(TEST_FILE_PATH) ) > 0)

if __name__ == '__main__':
    unittest.main()
