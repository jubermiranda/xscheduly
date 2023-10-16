"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import os
import sys
import zipfile
import xml.etree.ElementTree as ElTree

def extract_content_from_odt(file_path):
    content = []
    try:
        with zipfile.ZipFile(file_path, 'r') as odt_file:
            content = ElTree.fromstring(odt_file.read('content.xml'))
    except Exception as e:
        print("ODT FILE READ ERROR")

    return content

def find_tables_from_content(content):
    namespaces = {
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
        'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    }
    x_path_table = './/table:table'

    tables = content.findall(x_path_table, namespaces)
    return tables

def process_tables(tables):
    data_from_tables = {
        "teachers": [],
        "subjects": []
    }

    for table in tables:
        # TODO: Determine se a tabela pertence a professores ou matérias
        # e adicione os dados à lista apropriada em data_from_tables.
        # Exemplo: verificar o conteúdo da tabela para decidir.
        pass

    return data_from_tables

class OdtTableExtractor:
    def __init__(self, file_path):
        self.tables = []
        self.file_path = file_path

    def get_tables(self):
        try:
            self.tables = process_tables(find_tables_from_content(extract_content_from_odt(self.file_path)))
        except Exception as e:
            print("Error reading odt file")

        return self.tables

