import csv
import datetime
import os
import sys


def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu(error=None):
    """Work log main menu"""
    clear()
    welcome_message = '-  Your Electronic Timesheet  -'
    border = '-' * len(welcome_message)
    print(border)
    print(welcome_message)
    print(border)

    # If error print error else blank line
    error = f'\n[!] {error} Please select again \n' if error else ''
    print(error)

    for key, value in MENU.items():
        print(f'{key}) {value.__doc__}')

    user_input = input('>')

    if user_input in MENU:
        MENU[user_input]
    else:
        main_menu(error='Incorrect input.')

    return None


def add_task():
    """Add new task"""
    pass


def search_task():
    """Search for a task"""
    pass


def exit_program():
    """Exit work log"""
    # add any clean up that needs to happen here
    sys.exit()


MENU = {
    'a': add_task,
    'b': search_task,
    'c': exit_program,
}


if __name__ == '__main__':

    # Main menu
    main_menu()
