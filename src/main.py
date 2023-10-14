
# MODULES
from subject.subject import Subject
from teacher.teacher import Teacher
from xscheduly_manager.xscheduly_manager import XschedulyManager

manager = None

def main():
    try:
        instantiate_modules()

    except Exception as e:
        print("An error occurred:", str(e))

    try:
        result = manager.verify_file_format("teachers_and_subjects.csv")
        print(f"[{result}]")

    except Exception as e:
        print("An error occurred:", str(e))






def instantiate_modules():
    global manager
    manager = XschedulyManager()

if __name__ == "__main__":
    main()

