"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import os
import sys
import zipfile
import xml.etree.ElementTree as ET

class OdtTableExtractor:
    def __init__(self):
        pass

    def check_content_format(file_path):
        try:
            with zipfile.ZipFile(file_path, 'r') as odt:

                content_xml = odt.read('content.xml')
                root = ET.fromstring(content_xml)

                namespaces = {
                    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
                    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
                }

                table_elements = root.findall('.//table:table', namespaces)

                return len(table_elements) > 0

        except Exception as e:
            print(f"Error while checking for tables: {str(e)}")
            return False


