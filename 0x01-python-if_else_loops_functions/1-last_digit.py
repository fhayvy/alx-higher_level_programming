#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)
last_index = str_number[-1]
last_digit = int(last_index)
message = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    print(f"{message} and is greater than 5")
elif last_digit == 0:
    print(f"{message} and is 0")
else:
    print(f"{message} and is less than 6 and not 0")
