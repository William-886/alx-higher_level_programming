#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c = set_1.difference(set_2)
    d = set_2.difference(set_1)
    return c.union(d)
