import getpass
from key import get_key
from random_password import id_generator

master_pwd = getpass.getpass("Enter Master Password: \n")
master_key = get_key(master_pwd.encode())


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            account, user, passw = data.split("|")
            print("Account:", account)
            try:
                print("User:", user)
                print("Password:", master_key.decrypt(passw.encode()).decode())
            except:
                # print random password if the master key is incorrect
                print("User:", id_generator(6))
                print("Password:", id_generator())
            print("_______________")
    pass


def add():
    name = input("Account Name: ")
    user = input("User Name: ")
    pwd = getpass.getpass("Password: ")

    with open("passwords.txt", "a") as f:
        token = master_key.encrypt(pwd.encode())
        f.write(name + "|" + user + "|" + str(token.decode()) + "\n")
    pass


while True:
    mode = input("(V)iew (A)dd (Q)uit\n").lower()

    if mode == "q":
        break

    if mode == "a":
        add()
    elif mode == "v":
        view()
    else:
        print("Invalid input")
        continue
