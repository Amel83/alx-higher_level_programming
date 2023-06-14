#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for x in set(my_list):
        sum += x
    return (sum)
