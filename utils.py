import csv
import os

# get absolute path for 'work_log.csv'
filename = os.path.join(
    os.path.abspath(os.curdir),
    'work_log.csv'
)


def initialize_csv():
    """
    Creates 'work_log.csv' if it does not already exist
    :return: None
    """
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf8') as outfile:
            outfile.write('')
    return None


def read_csv():
    """Reads 'work_log.csv' into memory"""
    with open(filename, encoding='utf8') as infile:
        data = [row for row in csv.DictReader(infile)]
    return data

# read csv

# write csv

# append to csv
