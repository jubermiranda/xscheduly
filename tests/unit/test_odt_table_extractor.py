"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import unittest
import os
import sys

sys.path.append(os.path.abspath('../../src'))

from src.xscheduly_manager.odt_table_extractor import OdtTableExtractor

class OdtTableExtractor:
    def setUp(self):
        self.extractor = OdtTableExtractor()

    def test_file_format_correct(self):
        assertTrue(False)



