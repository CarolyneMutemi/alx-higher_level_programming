#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) - 1 == 0:
        print(f"0 arguments.")

    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        print(f"{len(argv) - 1}: " + argv[1])

    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for a in range(1, len(argv)):
            print(f"{a}: {argv[a]}")
