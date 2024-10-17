import os

file_path = "salt.key"


def check_if_existing():
    if os.path.exists(file_path):
        return True
    else:
        return False
