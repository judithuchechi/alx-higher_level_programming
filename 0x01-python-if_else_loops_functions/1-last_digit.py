#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

if (number > 0):
	num = (number % 10) * 1
elif (number < 0):
	num = (number % -10) * 1

if (number % 10) > 5:
	print(f"Last digit of {number} is {num} and is greater than 5")
elif (number % 10) == 0:
	print(f"Last digit of {number} is {num} and is 0")
elif ((number % 10) < 6 and not 0):
	print(f"Last digit of {number} is {num} and is less than 6 and not 0")
print(end= '')
