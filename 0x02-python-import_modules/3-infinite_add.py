#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    b = 0
    for c in range(len(sys.argv) - 1):
        b = b + int(sys.argv[c + 1])
    print(b)
