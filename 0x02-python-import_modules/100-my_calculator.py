#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if (num_args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (sys.argv[2] == '+'):
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(int(sys.argv[1]), int(sys.argv[3]))))
    elif (sys.argv[2] == '-'):
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif (sys.argv[2] == '*'):
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif (sys.argv[2] == '/'):
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(int(sys.argv[1]), int(sys.argv[3]))))
    else:
        print("{}".format("Unknown operator. Available operators: +, -, * and /"))
        exit(1)
