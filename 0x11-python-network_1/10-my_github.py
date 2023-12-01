#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]

    url = 'https://api.github.com/user'
    data = requests.get(url, auth=(user, pwd))
    print(data.json().get('id'))
