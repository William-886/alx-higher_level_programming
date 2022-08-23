#!/usr/bin/python3
for a in range(0, 100):
    if a < 10:
        print(f"{a:02}, ", end="")
    elif a > 9 and a < 99:
        print(f"{a}, ", end="")
    else:
        print(a)
