#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if j < 8:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j), end="")
            if i == 8 and j == 9:
                print("")
                break
            else:
                print(", ", end="")
