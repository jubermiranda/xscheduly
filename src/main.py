import csv
import time

# MODULES
from subject.subject import Subject
from teacher.teacher import Teacher
from xscheduly_manager.xscheduly_manager import XschedulyManager

def main():
    try:
        result = verify_file_format("teachers_and_subjects.csv")
        print(f"[{result}]")

    except Exception as e:
        print("An error occurred:", str(e))

def verify_file_format(file_path):
    print("Checking file format", end="")
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(0.025)

    if validate_csv_file(file_path):
        return "OK"
    else:
        return "FORMAT_ERROR"

def validate_csv_file(file_path):
    # Add your CSV validation logic here
    # Return True if valid, False if not
    return True

if __name__ == "__main__":
    main()

