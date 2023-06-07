#!/usr/bin/python3
output = ""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if j < 8:
            output += "{:d}{:d}, ".format(i, j)
        else:
            output += "{:d}{:d}".format(i, j)
            if i == 8 and j == 9:
                output += ""
                break
            else:
                output += ", "
print(output)
