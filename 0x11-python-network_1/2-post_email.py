#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response
"""

import sys
from urllib import request, parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    params = {'email': email}
    params = parse.urlencode(params).encode('utf-8')
    url = request.Request(url, params)
    with request.urlopen(url) as data:
        print(data.read().decode('utf-8'))
