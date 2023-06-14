#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    sum = 0
    num = 0
    for var in my_list:
        sum += (var[0] * var[1])
        num += var[1]
    return (sum / num)
