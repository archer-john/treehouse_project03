import datetime
import os
import sys

from add_task import add_task
from search_task import search_task
from utils import initialize_csv, clear, menu_header


def main_menu(error=None):
    """Work log main menu"""
    clear()
    menu_header()

    # If error print error else blank line
    error = f'\n[!] {error} Please select again \n' if error else ''
    print(error)

    for key, value in MENU.items():
        print(f'{key}) {value.__doc__}')

    user_input = input('>')

    if user_input in MENU:
        MENU[user_input]()
    else:
        main_menu(error=f'Incorrect input (last input: {user_input}).')

    return None


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

    # Initialize csv
    initialize_csv()

    # Main menu infinite loop
    while True:
        main_menu()
