# I'm going to use the info table html as a guide
import csv

def ready_printing():
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel-tab')
        writer.writerow(gen_header())

def print_row(data):
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel-tab')
        writer.writerow(data.values())

def gen_header():
    header = []
    header.append('Name of Issuer')
    header.append('Title of Class')
    header.append('CUSIP')
    header.append('Value(x$1000)')
    header.append('SH/PRN Amount')
    header.append('SH/PRN')
    header.append('PUT/CALL')
    header.append('Investment Discretion')
    header.append('Other Manager')
    header.append('Sole Voting Authority')
    header.append('Shared Voting Authority')
    header.append('None Voting Authority')
    return header
