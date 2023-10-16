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

TEST_FILE_PATH = "templates/table_test.odt"

class TestOdtTableExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = OdtTableExtractor(TEST_FILE_PATH)

    def test_get_data_objects(self):
        data = self.extractor.get_data_objects()

        # Verifique se o retorno é uma tupla
        self.assertIsInstance(data, tuple)

        # Verifique se a tupla contém duas listas
        self.assertEqual(len(data), 2)
        self.assertIsInstance(data[0], list)
        self.assertIsInstance(data[1], list)

        # Aqui você pode verificar se as listas estão preenchidas corretamente com objetos reais
        # Por exemplo, verifique se a primeira lista contém objetos Teacher e a segunda lista contém objetos Subject.

