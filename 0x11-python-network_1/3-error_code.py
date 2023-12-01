#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with request.urlopen(url) as data:
            print(data.read().decode('utf-8'))
    except Exception as e:
        print(f'Error code: {e.code}')
