# I'm going to use the info table html as a guide

# Name of issuer
# Title of class
# CUSIP
# Value(x$1000)
# Shrs or PRN AMT / Type
# SH/PRN
# Investment Discretion
# Other manager
# Voting authority
    # Sole
    # Shared
    # None

def pretty_print(root):
    print_header()
    for infotable in root:
        line = []
        for text in infotable:
            toInsert = text.text
            if toInsert == '\n':
                for subtext in text:
                    line.append(subtext.text)
                continue
            line.append(toInsert)
        print('\t'.join(line))


def print_header():
    header = ''
    for i in range(8):
        header += 'Column ' + str(i + 1) + '\t'
    header += '\n'
    header += '\t\t\t' * 2
    header += 'Value\t\tSHRS OR SH/\tInvestment\tOther\t\tVoting authority'

    header += '\n'
    header += 'Name Of Issuer\tTitle Of Class\tCUSIP\t\t'
    header += ' (X$1000)\tPRN AMT\tPRN\tDiscretion\t'
    header += 'Manager\t\tSole\tShared\tNone'
    print(header)
