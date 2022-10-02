#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    addition = 0
    for a in range(1, len(argv)):
        addition += int(argv[a])
    print(addition)
