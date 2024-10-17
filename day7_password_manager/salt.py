import os

from check_file_if_exist import check_if_existing


def get_salt():
    file_exists = check_if_existing()

    if file_exists == False:
        key = os.urandom(16)
        with open("salt.key", "wb") as key_file:
            key_file.write(key)
        return key
    else:
        with open("salt.key", "rb") as key_file:
            key = key_file.read()
            return key
