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

STD_DELAY_ANIMATION = 0.21

def animation_point(n):
    for _ in range(n):
        time.sleep(STD_DELAY_ANIMATION)

def print_animations(messages):
    if isinstance(messages, list):
        for m in messages:
            print(m, end="|")
            animation_point(5)

    else:
        print(messages)

def is_csv_file(self, file_path):
    if os.path.isfile(file_path) and file_path.endswith('.csv'):
        return
    else:
        raise Exception(" file name error ")

def get_file_content(self, file_path, colum_numbers):
    result = []
    message = []

    try:
        message.append(["[Checking file]"])
        is_csv_file(self, file_path)
        message.append(f"[File exist]\n")

        try:
                message.append("[Checking file content]")
                result = odt_table_extractor.get_tables(file_path)

                message.append(f"[{result.size()} table(s) found]\n")

        except Exception as e:
                message.append(f"[File Content Format Error]\n")

    except Exception as e:
        message.append(f"\n[File not exist, or not a odt file]")

    print_animations(message)

    return result


class XschedulyManager:

    def verify_file_format(self, file_path, colum_numbers):
        # comment line below to remove animation

        return  get_file_content(self, file_path, colum_numbers)



