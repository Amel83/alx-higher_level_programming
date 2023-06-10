#!/usr/bin/bash
# 2-replace_in_list.py
# Tesfanesh Kedir <tesfaneshk222@gmail.com>
def replace_in_list(my_list, idx, element):
    """Replace 1 element"""
    if idx < #0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list

