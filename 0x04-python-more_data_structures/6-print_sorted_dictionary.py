#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_key = {k: v for k, v in sorted(a_dictionary.items())}
    for i in sort_key:
        print("{}: {}".format(i, sort_key[i]))
