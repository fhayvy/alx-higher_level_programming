#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv)
    result = 0
    for i in range(1, num_args):
        result += int(sys.argv[i])
    print("{}".format(result))
