#!/usr/bin/python3
out = ""
for i in range(0, 100):
    if i != 99:
       out += f"{i:02}, "
    else:
        out += "99"
print(out)
