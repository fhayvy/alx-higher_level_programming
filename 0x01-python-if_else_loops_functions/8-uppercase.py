#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            result += chr(ord(str[i]) - 32)
        else:
            result += str[i]

        print("{}".format(result))
