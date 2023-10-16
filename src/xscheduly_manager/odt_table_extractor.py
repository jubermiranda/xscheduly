"""
Module to read odt file, search for tables
provide mothods to create csv tables from
tables found inside odt fiel
"""
import os
import zipfile
import xml.etree.ElementTree as ElTree

def find_tables_element(content):
    namespaces = {
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
        'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    }
    x_path_table = './/table:table'

    return content

def extract_content_from_odt(file_path):
    content = None
    try:
        with zipfile.ZipFile(file_path, 'r') as odt_file:
            content = ElTree.fromstring(odt_file.read('content.xml'))
    except Exception as e:
        print("ODT FILE READ ERROR")

    return content

def gen_tables(file_path):
    table_element = find_tables_element(extract_content_from_odt(file_path))

    # Assume que o conteúdo da tabela está dentro de 'table:table-row'
    namespaces = {
        'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    }
    x_path_row = './/table:table-row'
    rows = table_element.findall(x_path_row, namespaces)

    table_content = []
    for row in rows:
        # Assume que o conteúdo da célula está dentro de 'table:table-cell'
        x_path_cell = './/table:table-cell'
        cells = row.findall(x_path_cell, namespaces)

        row_data = []
        for cell in cells:
            # Assume que o conteúdo de texto está dentro de 'text:p'
            x_path_text = './/text:p'
            texts = cell.findall(x_path_text, namespaces)

            cell_data = ""
            for text in texts:
                cell_data += text.text + " "  # Você pode ajustar a formatação conforme necessário

            row_data.append(cell_data.strip())  # Remove espaços em branco

        table_content.append(row_data)

    return table_content

def create_teacher():
   return []

def create_subject():
    return []

def get_data_objects(tables):
    teachers = []
    subjects = []

    for table in tables:
        # Process the table and create Teacher and Subject objects
        teacher = create_teacher(table)
        subject = create_subject(table)

        teachers.append(teacher)
        subjects.append(subject)

    return teachers, subjects

class OdtTableExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data_objects(self):
        data = get_data_objects(gen_tables(self.file_path))


