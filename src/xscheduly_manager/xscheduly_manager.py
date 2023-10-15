"""
Xscheduly Manager Module

This module provides tools to manage general operations in app Xscheduly 
It includes functionality for handling subjects, teachers, and scheduling operations.

Classes:
    - `XschedulyManager`: Manages the scheduling of subjects with available teachers.
    - `OdtTableExtractor`: Provides functionality to extract tables from .odt files 


Usage:
    You can use this module to create and manage subjects, teachers, and schedule 
    them using the provided classes and functions.
"""
import time

def init_manager():
    pass

def validate_csv_file(file_path):
    # TODO("write logic ")
    return True

class XschedulyManager:
    def __init__(self):
        init_manager()


    def verify_file_format(self, file_path):
        print("Checking file format", end="")
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.025)

        if validate_csv_file(file_path):
            print("[OK]")
        else:
            raise Exception("Format error")
