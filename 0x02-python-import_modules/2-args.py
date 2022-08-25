#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = sys.argv
    n = 1
    if len(c) == 1:
        print("{} arguments.".format(len(c) - 1))    
    elif len(c) == 2:
        print("{} argument:".format(len(c) - 1))
        for a in range(1, len(c)):
            print("{}: {}".format(a, c[n]))
    elif len(c) > 2:
        print("{} arguments:".format(len(c) - 1))
        for a in range(1, len(c)):
            print("{}: {}".format(a, c[n]))
            n += 1
