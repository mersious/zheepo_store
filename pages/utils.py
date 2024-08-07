import os

INVALID_INPUT = -1

def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")