#!/usr/bin/python3
"""
Lists 10 commits of the repo rails by user rails.
"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    data = requests.get(url)
    lis = sorted(data.json(),
                 key=lambda x: x['commit']['author']['date'],
                 reverse=True)

    count = 1
    for dic in lis:
        print("{}: {}"
              .format(dic.get('sha'),
                      dic.get('commit').get('author').get('name')))
        if count == 10:
            break
        count += 1
