import FHParser.parser
import FHParser.printer

test_CIK = '0001166559'
archive_gen = FHParser.parser.find_13f_archive(test_CIK)
if archive_gen == None:
    exit()

data = FHParser.parser.find_13f_actual(next(archive_gen))
FHParser.printer.pretty_print(data)
