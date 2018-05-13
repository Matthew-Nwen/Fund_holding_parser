import FHParser.parser
import FHParser.printer
import sys

if len(sys.argv) < 2:
    print("Please insert a valid CIK/Ticker as a command line argument.")
    exit()

CIK = sys.argv[1]

curr = None
try:
    processing = sys.argv[2]
    curr = 1
except:
    pass

for archive_link in FHParser.parser.find_13f_archive(CIK):
    if archive_link == None:
        print('No 13F forms found.')
        exit()

    try:
        FHParser.printer.ready_printing(curr)
    except:
        print("Error printing to file.")
        exit()

    for data in FHParser.parser.find_13f_actual(archive_link):
        FHParser.printer.print_row(curr, data)

    if not curr:
        break
    curr += 1

print("Finished scraping 13F forms.")
print("Goodbye!")

"""
try:
    FHParser.printer.ready_printing('')
except:
    print("Error printing to file.")
    exit()

for data in FHParser.parser.find_13f_actual('https://www.sec.gov/Archives/edgar/data/1166559/000104746909007831/0001047469-09-007831.txt'):
    FHParser.printer.print_row('', data)
"""
