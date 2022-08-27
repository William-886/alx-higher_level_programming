#!/usr/bin/python3
def multiple_returns(sentence):
    # my_string = ' '.join(map(str, sentence))
    length = len(sentence)
    first_c = sentence[0]
    if length <= 1:
        first_c = 'None'
    return (length, first_c)
