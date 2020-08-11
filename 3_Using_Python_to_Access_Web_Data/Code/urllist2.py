import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
pos = int(input('Enter position: '))
count = int(input('Enter count: '))

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup =BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[pos-1].get('href', None)
    name = tags[pos-1].get_text()
    print(i, name, link)
    url = link