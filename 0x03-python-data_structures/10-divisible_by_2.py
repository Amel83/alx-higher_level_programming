#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_no = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_no.append(True)
        else:
            even_no.append(False)
    return even_no
