import requests
from bs4 import BeautifulSoup
import re

test_CIK = '0001166559'
browse_url = 'https://www.sec.gov/cgi-bin/browse-edgar'
archive_url = 'https://www.sec.gov'

# Not sure if regex matching is the best idea.
def verify_CIK(CIK):
    digits = re.compile(r'\b(\d){10}\b')
    if digits.match(CIK):
        return True
    ticker = re.compile(r'\b([a-zA-z]){4}[X]\b')
    if ticker.match(CIK):
        return True
    return False


def find_13f(CIK):
    if !verify_CIK(CIK):
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

    links = soup.find_all('a')
    for link in links:
        link = str(link)
        if 'document' in str.lower(link):
            archive_link = link.split(' ')[1]
            archive_link = archive_link.replace('href=', '')
            archive_link = archive_link.replace('"', '')
            yield (archive_url + archive_link)
