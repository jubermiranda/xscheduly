"""
Xscheduly Manager Module

This module provides tools to manage general operations in app Xscheduly 
It includes functionality for handling subjects, teachers, scheduling operation.
this module provide functions to import data fom csv file.

Usage:
    You can use this module to create and manage subjects, teachers, and schedule 
    them using the provided classes and functions.
"""
import time
import os

from . import odt_table_extractor

STD_DELAY_ANIMATION = 0.01

def animation_delay(n):
    for _ in range(n):
        time.sleep(STD_DELAY_ANIMATION)

def print_animations(messages):
    if isinstance(messages, list):
        for m in messages:
            print(m)
            animation_delay(4)

    else:
        print(messages)

def is_odt_file(self, file_path):
    return os.path.isfile(file_path) and file_path.endswith('.odt')


def get_file_content(self, file_path, colum_numbers):
    tables = []

    try:
        tables = odt_table_extractor.get_tables(file_path, colum_numbers)

    except Exception as e:
        print(e)

    return tables

class XschedulyManager:

    def verify_file_format(self, file_path):
        message = []
        message.append(f"[Checking file]")

        if is_odt_file(self, file_path):
            message.append(f"[File exist]")
        else:
            message.append(f"[File not exist, or not a odt file]")
            return False

        print_animations(message)
        return True

