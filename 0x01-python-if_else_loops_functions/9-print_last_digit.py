#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number."""
    mod = number % 10
    if number < 0:
        mod = (number * -1) % 10
    print("{}".format(mod), end="")
    return mod
