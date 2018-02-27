import datetime

from utils import append_csv, clear


def get_date():
    """
    By default use today's date, or allow the user enter a data using
    DD/MM/YYYY format, validate that the user input is in the correct format
    and that it is in fact a proper date
    :return: str
    """
    error = False
    while True:
        clear()
        today = datetime.datetime.now().strftime('%d/%m/%Y')
        print(f'Leave blank to use today\'s date: {today}')
        print('or enter a date using DD/MM/YYYY format')
        if error:
            print(f'[!] Incorrect date used (last input: {user_date}).')
        user_date = input('>')

        # Validate user input
        if not user_date:
            return today
        else:
            try:
                datetime.datetime.strptime(user_date, '%d/%m/%Y')
            except ValueError:
                error = True
                continue
            else:
                return user_date


def get_title():
    """
    Request user to enter a title for the task, validate that this value is not
    empty
    :return: False if validation fails else str
    """
    error = False
    while True:
        clear()
        print('Enter a Task title')
        if error:
            print('[!] You must provide a task title!')
        title = input('>')
        if title:
            return title
        error = True


def get_time_spent():
    """
    Request user to enter time spent on task, validate that
    the value is not blank, is an integer, and greater than 0
    :return: False if validation fails else str
    """
    error = False
    while True:
        clear()
        print('Enter time spent on task in rounded minutes')
        if error:
            print(f'[!] Can not be blank, be at least 1 minute and be '
                  f'rounded minutes! (last input {time})')
        time = input('>')
        if time and time.isdigit():
            if int(time) > 0:
                return time
        error = True


def add_task():
    """Add new task"""

    task = {
        'date': get_date(),
        'title': get_title(),
        'time': get_time_spent()
    }
    # get notes from user
    clear()
    print('Enter a note for this task (can be left blank)')
    task['notes'] = input('>')

    append_csv(task)
    clear()
    input('Your task has been saved. Press enter to continue to the main menu.')

    return None
