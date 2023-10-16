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
        self.extractor = OdtTableExtractor(TEST_FILE_PATH)

    def test_get_tables_from_odt_file_template_should_return_2_tables(self):
        tables =  self.extractor.get_tables_from_odt_file() 
        print(f"\nTables: {tables}")
        self.assertTrue(len(tables) == 2)

if __name__ == '__main__':
    unittest.main()
