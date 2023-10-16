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

def process_table_to_objects(table):
    # Aqui você pode processar e formatar a tabela como desejado, como extrair informações específicas
    # de linhas e células e criar uma representação das turmas da faculdade.
    # Por exemplo, você pode criar instâncias de classes para representar o conteúdo da tabela.

    # O exemplo a seguir apenas retorna o elemento XML da tabela formatado.
    return ElTree.tostring(table, encoding='unicode')

def process_tables(tables):
    data_from_tables = []

    for table in tables:
        formatted_table = process_table_to_objects(table)
        data_from_tables.append(formatted_table)

    return data_from_tables

class OdtTableExtractor:
    def __init__(self, file_path):
        self.tables = []
        self.file_path = file_path

    def get_tables_from_odt_file(self):
        try:
            xml_content = extract_content_from_odt(self.file_path)
            self.tables = find_tables_from_content(xml_content)
        except Exception as e:
            print("Error reading odt file")

        return self.tables

