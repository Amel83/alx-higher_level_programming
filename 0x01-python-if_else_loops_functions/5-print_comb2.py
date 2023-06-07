#!/usr/bin/python3
out = ""
for i in range(100):
    if i < 99:
       out += "{:02d}, ".format(i)
    else:
        out += "99"
print(out)
