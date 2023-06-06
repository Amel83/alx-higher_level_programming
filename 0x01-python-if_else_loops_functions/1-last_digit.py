#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digitt = -1 * digit
else:
    digitt = digit
print(f"Last digit of {number} is {digitt}", end='')
if digitt > 5:
    print(" and is greater than 5")
elif digitt == 0:
    print(" and is 0")
if digitt < 6 and digitt != 0:
    print(" and is less than 6 and not 0")
