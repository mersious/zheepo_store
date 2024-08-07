import os
import sys

sys.path.insert(0, os.path.join(__file__, "../../"))

from management import management
from utils import *

def print_main_menu():
        print("1- Management")
        print("2- Customer")
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

def render():
        global INVALID_INPUT
        print("Welcome to Zheepo Store")
        options = print_main_menu()
        user_request = get_user_selection(options)
        match user_request:
                case 1:
                        management.run()
                case 2:
                        print("Customer")
                case 'e':
                        exit("Have a nice day ^__^")
                case INVALID_INPUT:
                        pass
        clear_screen()
        

