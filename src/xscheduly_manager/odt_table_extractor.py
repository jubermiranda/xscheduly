"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import os
import sys
import zipfile
import xml.etree.ElementTree as ElTree

def get_odt_content(self):
    try:
        with zipfile.ZipFile(self.file_path, 'r') as odt_file:
            
            namespaces = {
                'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
                'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
            }
            x_path_table = './/table:table'

            tables = ElTree.fromstring(odt_file.read('content.xml')).findall(x_path_table, namespaces)
            return tables

    except Exception as e:
        return []



class OdtTableExtractor:
    def __init__(self, file_path):
        self.tables = []
        self.file_path = file_path

    def get_tables_from_odt_file(self):
        try:
            self.tables = extract_content_from_odt
            # TODO:
            # separe as responsabilidades do metodo em 2. um extrai element_tree outro procura no element_tree por tables
                            
        except Exception as e:
            print("Error reading odt file")

        return tables


