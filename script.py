import urllib.request
import re

url = 'https://www.istockphoto.com/photos/pathology-microscope'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'https://media\.istockphoto\.com/id/[^\"]+', html)
    if match:
        print(match.group(0))
    else:
        print("Not found")
except Exception as e:
    print(e)
