#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        first_char = sentence[0]
        length = len(sentence)
        return (length, first_char)
    else:
        return (0, None)
