#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    if len(my_list) > 0:
        c = my_list[0]
        for b in range(1, len(my_list)):
            if my_list[b] > c:
                c = my_list[b]
        return(c)
    else:
        return None
    """
    if len(my_list) > 0:
        my_list.sort()
        return (my_list[-1])
    else:
        return None
