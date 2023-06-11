#!/usr/bin/python3
def no_c(my_string):
    k = ''
    for i in my_string:

        if i != 'c' and i != 'C':
            k += i
    return k
