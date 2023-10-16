"""
test xscheduly_manager module

This module test functionalities of xscheduly_manager
insite template dir have file(s) to use in tests

"""
import unittest
import os
import sys

sys.path.append(os.path.abspath('../../src'))
from src.xscheduly_manager.xscheduly_manager import XschedulyManager

TEST_FILE_PATH = "templates/table_test.csv"

class TestXschedulyManager(unittest.TestCase):
    def setUp(self):
        self.manager = XschedulyManager()

    def test_test_file_exists(self):
        self.assertTrue(os.path.exists(TEST_FILE_PATH))

    def test_file_should_be_in_odt_format(self):
        self.assertTrue(self.manager.verify_file_format(TEST_FILE_PATH))

    def test_load_data(self):
        data = self.manager.load_data()
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) > 0)
        self.assertTrue(len(data[1]) > 0)



if __name__ == '__main__':
    unittest.main()
