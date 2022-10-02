#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy = my_list.copy()
    b = 0
    for a in cpy:
        if a % 2 == 0:
            cpy[b] = True
        else:
            cpy[b] = False
        b += 1
    return cpy
