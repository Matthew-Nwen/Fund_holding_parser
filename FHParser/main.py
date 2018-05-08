import requests
import bs4

def ping_edgar():
    url = 'https://www.sec.gov/cgi-bin/browse-edgar'
    params = {'CIK': 'blah'}

    r = requests.get(url, params=params)
    return r

print(ping_edgar().text)
