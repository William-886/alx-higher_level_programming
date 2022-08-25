#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    c = sys.argv
    i = len(c) - 1
    n = 1
    if i == 0:
        print("{} arguments.".format(i))   
    elif i == 1:
        print("{} argument:".format(i))
    elif i > 1:
        print("{} arguments:".format(i))
    for a in range(1, len(c)):
        print("{}: {}".format(a, c[n]))
        n += 1
