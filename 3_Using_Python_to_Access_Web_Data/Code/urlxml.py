import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        url = 'http://py4e-data.dr-chuck.net/comments_876896.xml'

    data = urllib.request.urlopen(url, context=ctx).read()
    data.decode()
    try:
        tree = ET.fromstring(data)
    except:
        print('deserialize error')
        break

    nums = []
    counts = tree.findall('comments/comment/count')
    for count in counts:
        num = int(count.text)
        nums.append(num)
    print('Counts:', nums)
    Sum = sum(nums)
    print('Sum:', Sum)