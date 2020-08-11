import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_876897.json'

data = urllib.request.urlopen(url, context=ctx).read().decode()
info = json.loads(data)
nums = []
for pair in info['comments']:
    count = pair['count']
    nums.append(count)
Sum = sum(nums)
print(Sum)