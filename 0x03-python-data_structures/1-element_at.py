#!/usr/bin/python3

def element_at(my_list, idx):

    list_len = len(my_list)

    if idx < 0 and idx > list_len:
        return None
    elif idx < 0 or idx > list_len:
        return None
    else:
        return(my_list[idx])
