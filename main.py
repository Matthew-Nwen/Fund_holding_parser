import FHParser.parser
import FHParser.printer
import sys

if len(sys.argv) < 2:
    print("Please insert a valid CIK/Ticker as a command line argument.")
    print("This will scrape the most recent 13F filing, if possible.")
    print("Optionally, insert -A as a second argument to scrape all 13F docs.")
    exit()

CIK = sys.argv[1]
processing = None
curr = None
try:
    # TODO: Actually check for the right arg... argparse?
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
