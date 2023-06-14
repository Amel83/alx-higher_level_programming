#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    s = list(a_dictionary.keys())[0]
    biggest = a_dictionary[s]
    for j, num in a_dictionary.items():
        if num > biggest:
            big = num
            s = j
    return (s)
