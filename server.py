#!/usr/bin/py

import requests
import sys
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

if len(sys.argv) < 2:
    exit("Requires 1 argument")
url = "https://en.wikipedia.org/wiki/" + sys.argv[1]
website_url = requests.get(url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

My_table = soup.find('table',{'class':'infobox'})
lines = My_table.findAll('th')

for i in lines:
    print(cleanhtml(str(i)))


