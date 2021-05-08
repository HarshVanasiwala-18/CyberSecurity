import requests
from urllib2 import Request, urlopen, URLError

url = raw_input('Enter URL to check for Vulnerability - ')
req = Request(url)

response = urlopen(req)

headers = requests.get(url).headers

if 'Content-Security-Policy' in headers:
    print url + "\tNot Vulnerable to Content-Security-Policy"
else:
    print url + "\tis Vulnerable to Content-Security-Policy"

if 'Permissions-Policy' in headers:
    print url + "\tNot Vulnerable Permissions-Policy"
else:
    print url + "\tis Vulnerable to Permissions-Policy"

if 'X-Content-Type-Options' in headers:
    print url + "\tNot Vulnerable X-Content-Type-Options"
else:
    print url + "\tis Vulnerable to X-Content-Type-Options"

if 'Strict-Transport-Security' in headers:
    print url + "\tNot Vulnerable Strict-Transport-Security"
else:
    print url + "\tis Vulnerable to Strict-Transport-Security"

if 'Referrer-Policy' in headers:
    print url + "\tNot Vulnerable Referrer-Policy"
else:
    print url + "\tis Vulnerable to Referrer-Policy"

if 'X-Frame-Options' in headers:
    print url + "\tNot Vulnerable X-Frame-Options"
else:
    print url + "\tis Vulnerable to X-Frame-Options"
