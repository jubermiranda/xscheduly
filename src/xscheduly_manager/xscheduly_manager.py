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

from xscheduly_manager import odt_table_extractor

def animation_point(n):
    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(0.025)

def print_animations(messages, ms_delay):
    for m in messages:
        print(m)
        animation_point(ms_delay)

def is_csv_file(self, file_path):
    if os.path.isfile(file_path) and file_path.endswith('.csv'):
        return
    else:
        raise Exception(" file name error ")

def get_file_content(self, file_path, colum_numbers):
    result = []
    message = []

    try:
        is_csv_file(self, file_path)
        message.append("[File exist]")

        try:
                result = odt_table_extractor.get_tables(file_path)
                #all current check ok here after .get_tables
                #
                message.append(f"[{result.size()} table(s) found]")

        except Exception as e:
                message.append("[File Content Format Error]")

    except Exception as e:
        message.append("[File not exist, or not a odt file]")

    #coment line below to not print animations:
    print_animations(messages)

    return result


class XschedulyManager:

    def verify_file_format(self, file_path, colum_numbers):
        # comment line below to remove animation
        print_animations("[Checking file]", 3)

        return  get_file_content(self, file_path, colum_numbers)



