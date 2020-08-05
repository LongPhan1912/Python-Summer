# Extracting data from JSON

# Example code
# import json
#
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''
#
# info = json.loads(data)
# print('User count:', len(info))
#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

# assignment code
import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter link: ')
open_link = urllib.request.urlopen(link, context=ctx).read().decode()
data = json.loads(open_link)

sum = 0
for item in data['comments']:
    sum += item['count']

print(sum)
