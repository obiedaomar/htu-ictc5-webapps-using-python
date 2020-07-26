import urllib.request

import requests

url = "http://www.stackoverflow.com"

r = requests.get(url)

print(r.status_code)
print(r.url)
# print(r.json())
# print(r.text)
print(r.encoding)
