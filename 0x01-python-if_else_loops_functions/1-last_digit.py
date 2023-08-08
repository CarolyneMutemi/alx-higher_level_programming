#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if number < 0:
    mod = (number * -1) % 10
print("Last digit of", end=" ")
if mod > 5:
    print(f"{number} is {mod} and is greater than 5")
elif mod == 0:
    print(f"{number} is {mod} and is 0")
else:
    print(f"{number} is {mod} and is less than 6 and not 0")
