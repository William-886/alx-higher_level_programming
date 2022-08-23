#!/usr/bin/python3
def uppercase(str):
    for a in str:
        ascii = ord(a)
        if ascii >= 97 and ascii <= 122:
            ascii = ascii - 32
        print("{:c}".format(ascii), end="")
    print()
