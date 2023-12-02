#!/usr/bin/python3
"""
Lists 10 commits of the repo rails by user rails.
"""

import sys
import requests
from datetime import datetime

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    data = requests.get(url)
    lis = data.json()
    date_list = []
    today = datetime.now()

    count = 1
    for dic in lis:
        print(f"{dic.get('sha')}: \
              {dic.get('commit').get('author').get('name')}")
        if count == 10:
            break
        count += 1
