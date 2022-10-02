#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = number % 10
negative = -number % 10
if number >=0:
	if positive > 5:
		print(f"Last digit of {number} is {positive} and is greater than 5")
	elif positive == 0:
		print(f"Last digit of {number} is {positive} and is 0")
	else:
		print(f"Last digit of {number} is {positive} and is less than 6 and not 0")
else:
	if negative > 5:
		print(f"Last digit of {number} is {negative} and is greater than 5")
	elif negative == 0:
		print(f"Last digit of {number} is {negative} and is 0")
	else:
		print(f"Last digit of {number} is {negative} and is less than 6 and not 0")
