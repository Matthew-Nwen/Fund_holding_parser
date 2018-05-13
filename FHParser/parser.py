import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
import enum

# Links to EDGAR.
browse_url = 'https://www.sec.gov/cgi-bin/browse-edgar'
archive_url = 'https://www.sec.gov'

# Enum for which values to scrape for
class infotable_values(enum.Enum):
    nameofissuer = 1
    titleofclass = 2
    cusip = 3
    value = 4
    sshprnamt = 5
    sshprnamttype = 6
    putCall = 7
    investmentdiscretion = 8
    othermanager = 9
    sole = 10
    shared = 11
    none = 12

# Looks for the archive link to the submitted 13F form.
def find_13f_archive(CIK):
    if not verify_CIK(CIK):
        print('Error: invalid input.')
        return

    params = {'CIK': CIK, 'type': '13F'}
    response = requests.get(browse_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # This part feels a little hard coded.
    no_match_found = soup.find('h1')
    if no_match_found:
        print('No match found!')
        return

    for archive_link in gen_relevant_links(soup, 'document'):
        yield archive_url + archive_link

# With the link to the archive, parse the archived 13F text
def find_13f_actual(archive_url):
    actual_url = archive_url.replace('-index.htm', '.txt')
    response = requests.get(actual_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # With an infotable, the 13F is in a modern XML format.
    # Otherwise it's in an older ascii format!
    table = soup.find_all('infotable')
    if table:
        for table in soup.find_all('infotable'):
            yield gen_xml_line(table)
    elif not table:
        for line in handle_ascii_text(response.text):
            yield line

# Sends parsed data for a line from a single XML infotable on the modern 13F
def gen_xml_line(table):
    line = {}
    for search_query in infotable_values:
        try:
            line[search_query.name] = table.find(search_query.name).text
        except:
            line[search_query.name] = ''
            return line

# Processes ascii text for parsing and sending.
# Because the table is formatted as being left justfied to the start of a tag,
# I have to find the corrrect justification before parsing the data.
def handle_ascii_text(text):
    # Who thought text justifying by tags was a good idea....
    data = text.split('<Caption>')[1].split('\n') # TODO: is this split safe?
    justification = None
    for line in data:
        if justification:
            if line.startswith('</Table>'):
                break
            yield gen_ascii_line(line, justification)
        if not line.startswith('<'):
            continue
        justification = line
        justification = [i.start() for i in re.finditer('<', justification)]

# Sends parsed data for a line from a single ASCII line on the older 13F.
def gen_ascii_line(line, justification):
    result = {}
    for search_query in infotable_values:
        curr = search_query.value
        try:
            text = line[justification[curr-1]:justification[curr]].strip()
            result[search_query.name] = text
        except:
            result[search_query.name] = ''
    return result

# Checks if the input is either 10 digits or 5 char string ending in X
def verify_CIK(CIK):
    digits = re.compile(r'\b(\d){10}\b')
    if digits.match(CIK):
        return True
    ticker = re.compile(r'\b([a-zA-z]){4}[X]\b')
    if ticker.match(CIK):
        return True
    return False

# Generates all links that include some context string
def gen_relevant_links(soup, context):
    for link in soup.find_all('a'):
        link = str(link)
        if context in str.lower(link):
            # looks for the href attribute and returns what's between quotes
            link = re.search(r'"(.*?)"', link).group()
            link = link.replace('"', '')
            yield link
