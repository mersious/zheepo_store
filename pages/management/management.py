import os
import sys

sys.path.insert(0, os.path.join(__file__, "../"))

from utils import *

import csv

MANAGERS_FILE_PATH = os.path.join(__file__,"..\\data\\managers.csv")

def print_management_menu():
    print("1- Login")
    print("2- Sign Up")
    print("e- Back")
    options = ['1', '2', 'e']
    return options

def get_user_selection(options:list):
    user_input = input("Please Enter an Option: ")
    if (user_input.isalnum()) and (user_input in options):
            return user_input
    else:
            input("Invalid input! press any key to try again..")
            return INVALID_INPUT
    
def check_file_existance(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False
        
def write_data_to_file(data, file_path):
    if(not(check_file_existance(file_path))):
        with open(file_path, 'w', newline="") as managers_file:
            csv_writer = csv.writer(managers_file)
            csv_writer.writerow(data)
    else:
        with open(file_path, 'a', newline="") as managers_file:
            csv_writer = csv.writer(managers_file)
            csv_writer.writerow(data)   

def find_user(user, file_path):
    if(check_file_existance(file_path)):
        with open(file_path, 'r') as managers_file:
            csv_reader = csv.reader(managers_file)
            for row in csv_reader:
                if user[0] == row[0] and user[1] == row[1]:
                    return True
    return False

               
def sign_up():
    print("Sing UP")
    username = get_username()
    password = get_password(mode= "sign up")
    if username and password:
        write_data_to_file([username, password], MANAGERS_FILE_PATH)
        print("Signed up successfully!")
        input("Press any Key..")

def login():
    print("Login Section")
    username = get_username()
    password = get_password(mode= "login")
    if username and password:
        if find_user([username, password], MANAGERS_FILE_PATH):
            print(f"Welcome {username} ^___^")
            input("MAIN PAGE is loading..")
        else:
            print("user not found!")
            
         


def run():
    global INVALID_INPUT
    MANAGEMENT_RUNNING = True
    while MANAGEMENT_RUNNING:
        clear_screen()
        print("Management Panel")
        options = print_management_menu()
        user_request = get_user_selection(options)
        clear_screen()
        match user_request:
            case "1":
                    login()
            case "2":
                    sign_up()
            case 'e':
                    break
            case INVALID_INPUT:
                    pass
        clear_screen()
    
