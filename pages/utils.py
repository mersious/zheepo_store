import os

INVALID_INPUT = -1

def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

def get_username():
        while True:
            username = input("Username: ")
            username_length = len(username)
            if username_length < 8:
                   print("USERNAME length should be at least 8 characters.")
                   input("press any Key to try again..")
            elif username_length > 16:
                   print("USERNAME length is too long!")
                   input("press any Key to try again..")
            if username.isalnum():
                   return username
            else:
                   print("USERNAME")