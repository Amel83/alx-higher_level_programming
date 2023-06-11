#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list[0] < my_list[1]:
        a = my_list[1]
    else:
        a = my_list[0]
    if a < my_list[2]:
        b = my_list[2]
    else:
        b = a
    if b < my_list[3]:
        c = my_list[3]
    else:
        c = b
    if c < my_list[4]:
        d = my_list[4]
    else:
        d = c
    if d < my_list[5]:
        e = my_list[5]
    else:
        e = d
    if e < my_list[6]:
        f = my_list[6]
    else:
        f = e
    if f < my_list[7]:
        g = my_list[7]
    else:
        g = f
    return g
