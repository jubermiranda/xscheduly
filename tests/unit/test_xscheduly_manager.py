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


TEST_FILE_PATH = "templates/table_test.odt"
STD_COLUM_NUMBER = 2

class TestXschedulyManager(unittest.TestCase):
    def setUp(self):
        self.manager = XschedulyManager()

    def test_test_file_exists(self):
        self.assertTrue(os.path.exists(TEST_FILE_PATH))

    def test_file_should_be_in_odt_format(self):
        self.assertTrue(self.manager.verify_file_format(TEST_FILE_PATH, STD_COLUM_NUMBER))

if __name__ == '__main__':
    unittest.main()
