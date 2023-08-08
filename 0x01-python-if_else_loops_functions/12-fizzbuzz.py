#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100, \
            prints Fizz for mutiples of 3, \
            prints Buzz for mutliples of 5 and \
            FizzBuzz for mutiples of both 3 and 5."""
    for i in range(1, 101):
        mod3 = i % 3
        mod5 = i % 5
        if mod3 == 0 and mod5 == 0:
            print("FizzBuzz,", end=" ")
        elif mod3 == 0:
            print("Fizz", end=" ")
        elif mod5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
