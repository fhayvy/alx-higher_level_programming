#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    max_number = 0
    for i in my_list:
        if i > max_number:
            max_number = i
        else:
            max_number = max_number

    return (max_number)
