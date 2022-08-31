#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [item for item in my_list]
    for a in range(0, len(new_list)):
        if new_list[a] == search:
            new_list[a] = replace
    return (new_list)
