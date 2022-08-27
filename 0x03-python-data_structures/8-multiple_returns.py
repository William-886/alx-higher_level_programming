#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_c = sentence[0]
    if sentence == "":
        length = 0
        first_c = None
    return (length, first_c)
