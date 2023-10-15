import unittest
import os

from xscheduly_manager.odt_table_extractor import odt_table_extractor as extract_tables

file_path = 'test_data/table_test.odt'

class TestOdtTableExtractor(unittest.TestCase):

    def test_odt_file_exists(self):
        file_exists = os.path.exists(file_path)

        self.assertTrue(file_exists)


    def test_extract_tables_from_odt_should_return_2_tables(self):
        tables = extract_tables(file_path)

        self.assertIsNotNone(tables)
        self.assertEqual(len(tables), 2)

if __name__ == '__main__':
    unittest.main()

