import os

INVALID_INPUT = -1

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def check_username_validity(username):
    username_length = len(username)
    if username_length < 8:
        print("USERNAME length should be at least 8 characters.")
    elif username_length > 16:
        print("USERNAME length is too long!")
    elif username.isalnum():
        return True
    else:
        print("Invalid username.")
    input("press any Key to try again..")
    return False

def check_password_validity(password, mode = "sign up"):
    password_length = len(password)
    if password_length < 8:
        print("password length should be at least 8 characters.")
    elif password_length > 16:
        print("password length is too long!")
    elif password.isalnum():
        if mode == "sign up":
            pass_check = input("please re-enter your password: ")
            if password == pass_check:
                return True
            else:
                print("incorrect password!")
        else:
            return True
    else:
        print("Invalid password.")
    input("press any Key to try again..")
    return False

def get_username():
    while True:
        username = input("Username: ")
        if check_username_validity(username):
            return username
        clear_screen()
            
def get_password(mode):
    while True:
        password = input("Password: ")
        if check_password_validity(password, mode= mode):
            return password
        clear_screen()