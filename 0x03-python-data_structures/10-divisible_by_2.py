#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for s in range(0, len(my_list)):
        if my_list[s] % 2 == 0:
            new_list.insert(s, True)
        else:
            new_list.insert(s, False)
    return new_list
