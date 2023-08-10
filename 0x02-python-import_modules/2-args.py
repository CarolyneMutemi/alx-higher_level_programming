#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = 1
    n = len(sys.argv)
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        if n == 2:
            print("{:d} argument:".format(n - 1))
        else:
            print("{:d} arguments:".format(n - 1))
        while x < n:
            print("{:d}: {}".format(x, sys.argv[x]))
            x += 1
