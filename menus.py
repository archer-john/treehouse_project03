from utils import clear, exit_program
from add_task import add_task
from search_task import (find_by_date, find_by_exact_search,
                         find_by_pattern, find_by_time_spent)


def main_menu_header():
    welcome_message = '-  Your Electronic Timesheet  -'
    border = '-' * len(welcome_message)
    print(border)
    print(welcome_message)
    print('-' + ' ' * 9, 'Main Menu', ' ' * 9 + '-')
    print(border)


def search_menu_header():
    welcome_message = '-  Your Electronic Timesheet  -'
    border = '-' * len(welcome_message)
    print(border)
    print(welcome_message)
    print('-' + ' ' * 8, 'Search Menu', ' ' * 8 + '-')
    print(border)


def main_menu():
    """Main menu"""
    error = False
    while True:
        clear()
        main_menu_header()

        # If error print error else blank line
        if error:
            print(f'\n[!] Incorrect input (last input: {user_input}). '
                  f'Please select again \n')
        else:
            print()

        for key, value in MAIN_MENU.items():
            print(f'{key}) {value.__doc__}')

        user_input = input('>')

        if user_input in MAIN_MENU:
            MAIN_MENU[user_input]()
        else:
            error = True


def search_menu():
    """Search menu"""
    error = False
    while True:
        clear()
        search_menu_header()

        # If error print error else blank ling
        if error:
            print(f'\n[!] Incorrect input (last input: {user_input} '
                  f'Please select again. \n')
        else:
            print()

        for key, value in SEARCH_MENU.items():
            print(f'{key}) {value.__doc__}')

        user_input = input('>')

        if user_input in SEARCH_MENU:
            SEARCH_MENU[user_input]()
        else:
            error = True


MAIN_MENU = {
    'a': add_task,
    'b': search_menu,
    'c': exit_program,
}

SEARCH_MENU = {
    'a': find_by_date,
    'b': find_by_time_spent,
    'c': find_by_exact_search,
    'd': find_by_pattern,
    'e': main_menu,
}
