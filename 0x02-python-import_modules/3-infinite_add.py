#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    n = 1
    while n < len(sys.argv):
        sum += int(sys.argv[n])
        n += 1
    print(sum)
