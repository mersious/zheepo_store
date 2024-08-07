def print_main_menu():
        print("""
        1- Login
        2- Sign Up        
        e- Exit
        """)

def get_user_selection():
        user_input = input("Please Enter an Option: ")
        return int(user_input) 

def render():
        print("Welcome to Zheepo Store")
        print_main_menu()
        user_request = get_user_selection()
        match user_request:
                case 1:
                        print("Login ...")
                case 2:
                        print("Sign Up ...")
                case 'e':
                        exit("Have a nice day ^__^")
        

