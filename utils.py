import csv
import os

# get absolute path for 'work_log.csv'
filename = os.path.join(
    os.path.abspath(os.curdir),
    'work_log.csv'
)
# work_log.csv headers
HEADER = ['date', 'title', 'time', 'notes']


def initialize_csv():
    """
    Creates 'work_log.csv' if it does not already exist
    :return: None
    """
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=HEADER)
            writer.writeheader()
    return None


def read_csv():
    """
    Opens and reads 'work_log.csv'
    :return: List of OrderDicts
    """
    with open(filename, encoding='utf8') as infile:
        data = [row for row in csv.DictReader(infile)]
    return data


def write_csv(data):
    """
    Complete re-write of 'work_log.csv' with updated data
    :param data: List of OrderDicts
    :return: None
    """
    with open(filename, 'w', encoding='utf8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=HEADER)
        writer.writerows(data)
    return None


def append_csv(task):
    """
    Appends a task to the end of 'work_log.csv'
    :param task: Dict
    :return: None
    """
    with open(filename, 'a', encoding='utf8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=HEADER)
        writer.writerow(task)
    return None


def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
