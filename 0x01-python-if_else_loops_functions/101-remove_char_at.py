#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    j = 0
    for c in str:
        if j != n:
            copy += str[j]
        j += 1
    return copy
