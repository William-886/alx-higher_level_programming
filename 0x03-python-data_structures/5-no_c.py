#!/usr/bin/python3
def no_c(my_string):
    t_string = my_string.translate({ord('c'): None})
    new_string = t_string.translate({ord('C'): None})
    return (new_string)
