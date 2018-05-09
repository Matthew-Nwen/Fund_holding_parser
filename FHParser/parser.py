import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET

browse_url = 'https://www.sec.gov/cgi-bin/browse-edgar'
archive_url = 'https://www.sec.gov'

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

def find_13f_actual(archive_url):
    actual_url = archive_url.replace('-index.htm', '.txt')
    response = requests.get(actual_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # I dislike hard coding this. The first finding is just header info
    xml = soup.find_all('xml')[1]
    xml = format_xml(xml)
    root = ET.fromstring(xml)
    return root

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

def format_xml(xml):
    xml = str(xml)
    xml = xml.replace('<xml>', '')
    xml = xml.replace('</xml>', '')
    xml = xml.strip()
    return xml
