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
            return "OK"
        else:
            return "FORMAT_ERROR"



