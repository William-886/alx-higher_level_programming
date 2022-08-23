#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    a = 0
    for b in str:
        if n != a:
            new_str = new_str + b
        a = a + 1
    return (new_str)
