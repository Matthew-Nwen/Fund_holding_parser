import FHParser.parser
import FHParser.printer
import sys

CIK = '0001166559'
if len(sys.argv) > 1:
    CIK = sys.argv[1]
    # Should probably add something here in case I'm supposed to keep processing

archive_gen = FHParser.parser.find_13f_archive(CIK)
if archive_gen == None:
    # print('No 13F forms found.')
    exit()

data = FHParser.parser.find_13f_actual(next(archive_gen))
FHParser.printer.pretty_print(data)
