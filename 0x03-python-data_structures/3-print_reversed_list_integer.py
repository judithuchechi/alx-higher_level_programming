#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    length = len(my_list)
    idx = length - 1

    if my_list is None:
        return
    if not my_list:
        return
    else:
        for i in range(idx, -1, -1):
            print("{:d}".format(my_list[i]))
