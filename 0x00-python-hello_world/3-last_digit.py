#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {}".format(number), end="")
last_digit = int(repr(number)[-1])
if number > 0 or number == 0:
    print(" is {}".format(last_digit), end="")
    if last_digit > 5:
        print(" and is greater than 5")
    if last_digit < 6 and last_digit != 0:
        print(" and is less than 6 and not 0")
    if last_digit == 0:
        print(" and is 0")
if number < 0:
    print(" is -{}".format(last_digit), end="")
    print(" and is less than 6 and not 0")
    