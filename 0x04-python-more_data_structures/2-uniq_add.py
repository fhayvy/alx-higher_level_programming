#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum_total = 0

    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    for x in unique_list:
        sum_total += x

    return sum_total
