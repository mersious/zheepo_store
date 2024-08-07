import os
import sys

sys.path.insert(0, os.path.join(__file__, "../"))

from utils import *

def print_management_menu():
    print("1- Login")
    print("2- Sign Up")
    print("e- Exit")
    options = ['1', '2', 'e']
    return options

def get_user_selection(options:list):
        user_input = input("Please Enter an Option: ")
        if (user_input.isnumeric()) and (user_input in options):
                return int(user_input)
        elif user_input == 'e':
                return 'e'
        else:
                input("Invalid input! press any key to try again..")
                return INVALID_INPUT

def run():
    global INVALID_INPUT
    MANAGEMENT_RUNNING = True
    while MANAGEMENT_RUNNING:
        clear_screen()
        print("Management Panel")
        options = print_management_menu()
        user_request = get_user_selection(options)
        match user_request:
            case 1:
                    print("logining...")
            case 2:
                    print("sign uppping")
            case 'e':
                    break
            case INVALID_INPUT:
                    pass
        clear_screen()
    
