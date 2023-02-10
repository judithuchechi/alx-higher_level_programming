#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    list_len = len(my_list)
    new_list = []

    for num in my_list:
        for i in range(list_len):
            if my_list[i] % 2 == 0:
                new_list.append(True)
            elif my_list[i] % 2 != 0:
                new_list.append(False)
        return(new_list)
