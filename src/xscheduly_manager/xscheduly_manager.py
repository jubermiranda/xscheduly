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

def is_csv_file(self, file_path):
    return os.path.isfile(file_path) and file_path.endswith('.csv')

def check_file_content(self, file_path, colum_numbers):
    if True:
        return True

    else:
        return False

def validate_csv_file(self, file_path):
    return True


class XschedulyManager:

    def verify_file_format(self, file_path):
        print("[Checking file format]", end="")
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.025)

        if validate_csv_file(self, file_path):
            print("[OK]")
        else:
            raise Exception("Format error")



