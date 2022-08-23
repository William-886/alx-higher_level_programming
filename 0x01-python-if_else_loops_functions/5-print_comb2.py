#!/usr/bin/python3
for a in range(0, 100):
    if a < 10:
        print("{:02d}, ".format(a), end="")
    elif a > 9 and a < 99:
        print("{:d}, ".format(a), end="")
    else:
        print(a)
