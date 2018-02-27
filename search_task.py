from utils import work_log_by_date, clear


def search_results_header():
    welcome_message = '-  Your Electronic Timesheet  -'
    border = '-' * len(welcome_message)
    print(border)
    print(welcome_message)
    print('-' + ' ' * 6, 'Search  Results', ' ' * 6 + '-')
    print(border)


def find_by_date():
    """List dates with tasks"""
    log = work_log_by_date()
    error = False
    while True:
        index = 1
        clear()
        search_results_header()

        if error:
            print(f'\n[!] Incorrect input (last input: {user_input}). '
                  f'Please select again \n')
        else:
            print()

        for key, value in log.items():
            print(f'{index}) {key} # of tasks: {len(value)}')
            index += 1
        print('\nEnter a date to few that days tasks.')
        user_input = input('>')

        if user_input in log:
            for task in log[user_input]:
                clear()
                print(task['date'], task['title'], task['time'],
                      task['notes'], '\n')
                input('\nPress enter to return to the Search Menu.')
                return


def find_by_time_spent():
    """Search by time spent on task"""


def find_by_exact_search():
    """Search by exact date"""


def find_by_pattern():
    """Search by Regex"""



