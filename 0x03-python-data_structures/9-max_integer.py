#!/usr/bin/python3

def max_integer(my_list=[]):

    list_len = len(my_list)

    if list_len == 0:
        return None
    else:
        for i in range(list_len):
            i = list_len - 1
            while i > 1:
                j = 0
                while j < i:
                    if my_list[j] > my_list[j + 1]:
                        temp = my_list[j]
                        my_list[j] = my_list[j + 1]
                        my_list[j + 1] = temp
                    j = j + 1
                i = i - 1
        return(my_list[list_len - 1])
