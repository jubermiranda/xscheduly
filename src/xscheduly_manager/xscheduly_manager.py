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

def animation_point(n):
    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(0.025)

def is_csv_file(self, file_path):
    return os.path.isfile(file_path) and file_path.endswith('.csv')

def get_file_content(self, file_path, colum_numbers):
    if is_csv_file(self, file_path):
        animation_point(5)
        print(" File exist [OK]")
        return True
    else:
        return False

class XschedulyManager:

    def verify_file_format(self, file_path, colum_numbers):
        print("[Checking file]", end="")
        animation_point(5)

        return  get_file_content(self, file_path, colum_numbers)



