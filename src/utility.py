from os import name, system

""" Utility function to clear a terminal on all platforms """


def clear_terminal():
    if name == "nt":
        # Windows
        system("cls")
    else:
        # Linux / Mac
        system("clear")

