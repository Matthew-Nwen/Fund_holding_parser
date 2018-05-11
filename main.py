import FHParser.parser
import FHParser.printer
import sys

CIK = '0001166559'
if len(sys.argv) > 1:
    CIK = sys.argv[1]
    # TODO: keep processing flag?

archive_gen = FHParser.parser.find_13f_archive(CIK)
if archive_gen == None:
    # print('No 13F forms found.')
    exit()

# TODO: Process multiple forms?
data = FHParser.parser.find_13f_actual(next(archive_gen))

FHParser.printer.pretty_print(next(data))

# TODO: Write out to a file?
