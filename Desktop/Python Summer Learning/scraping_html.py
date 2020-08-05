# Code for scraping and extracting HTML data
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
pos = int(input('Enter position - '))
repeat = int(input('Enter times repeated - '))
name = None

tags = soup('a')
# tags with anchor; if you want 'span' tags, just type 'span' instead of 'a'
while repeat - 1 >= 0:
    target = tags[pos - 1]
    url = target.get('href', None)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    name = target.contents[0]
    repeat -= 1

print(name)
