import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# input interface
while True:
    address = input('Enter address: ')
    if len(address) < 1:
        address = 'Saint Petersburg State University'
    
    parm = {}
    if api_key is not False:
        parm['key'] = api_key
    parm['address'] = address
    url = serviceurl + urllib.parse.urlencode(parm)
    print('URL:', url)

    data = urllib.request.urlopen(url, context=ctx).read().decode()
    try:
        info = json.loads(data)
    except:
        info = None

    if not info or 'status' not in info or info['status'] != 'OK':
        print('Fail to retrieve data')
        print(data)
        break

    place_id = info['results'][0]['place_id']
    print('place_id:', place_id)