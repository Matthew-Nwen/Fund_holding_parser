# I'm going to use the info table html as a guide
import csv

def pretty_print(data):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(gen_header())
        writer.writerow(data.values())

# What to do on an empty field? Seems like this ignores gaps...
def add_text(text_element, line):
    toInsert = text_element.text
    if toInsert != '\n':
        line.append(toInsert)
        return
    for subtext in text_element:
        add_text(subtext, line)

def gen_header():
    header = []
    header.append('Name of Issuer')
    header.append('Title of Class')
    header.append('CUSIP')
    header.append('Value(x$1000)')
    header.append('SH/PRN Amount')
    header.append('SH/PRN')
    header.append('Investment Discretion')
#    header.append('Other Manager')
    header.append('Sole Voting Authority')
    header.append('Shared Voting Authority')
    header.append('None Voting Authority')
    return header
