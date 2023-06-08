#!/usr/bin/python3
if __name__ == "__main__":
    import math, sys
    j = 0
    for i in range(1, len(sys.argv)):
        j += int(sys.argv[i])
    print("{}".format(j))
