
# modules
from subject.subject import Subject
from teacher.teacher import Teacher

from xscheduly_manager.xscheduly_manager import XschedulyManager

MANAGER = None

def main():
    try:
        instantiate_modules()
    except Exception as e:
        print("An error occurred:", str(e))

    try:
        MANAGER.verify_file_format("teachers_and_subjects.csv")
    except Exception as e:
        print(str(e))




def instantiate_modules():
    global MANAGER
    MANAGER = XschedulyManager()

if __name__ == "__main__":
    main()
