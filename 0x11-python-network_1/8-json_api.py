#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    post = {'q': q}
    data = requests.post('http://0.0.0.0:5000/search_user', data=post)
    try:
        data_dict = data.json()
        if len(data_dict) == 0:
            print('No result')
        else:
            print(f"[{data_dict.get('id')}] {data_dict.get('name')}")
    except Exception:
        print('Not a valid JSON')
