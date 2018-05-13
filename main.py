import FHParser.parser
import FHParser.printer
import sys

if len(sys.argv) < 2:
    print("Please insert a CIK/Ticker as a command line argument.")
    exit()

CIK = sys.argv[1]
# TODO: keep processing flag?

archive_link = FHParser.parser.find_13f_archive(CIK)
if archive_link == None:
    # print('No 13F forms found.')
    exit()

# TODO: Process multiple forms?
try:
    FHParser.printer.ready_printing()
except:
    print("Error printing to file.")
    exit()

for data in FHParser.parser.find_13f_actual(archive_link):
    FHParser.printer.print_row(data)
