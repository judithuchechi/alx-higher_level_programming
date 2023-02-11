#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    new_tup = ()

    for i in range(2):
        if len(tuple_a) == 1 and len(tuple_b) == 1:
            tuple_a = (tuple_a[0], 0)
            tuple_b = (tuple_b[0], 0)
        if len(tuple_a) == 1 and len(tuple_b) == 2:
            tuple_a = (tuple_a[0], 0)
            tuple_b = (tuple_b[0], tuple_b[1])
        if len(tuple_a) == 2 and len(tuple_b) == 1:
            tuple_a = (tuple_a[0], tuple_a[1])
            tuple_b = (tuple_b[0], 0)
        if tuple_a == () and tuple_b == ():
            tuple_a = (0, 0)
            tuple_b = (0, 0)
        if tuple_a == () and len(tuple_b) == 2:
            tuple_a = (0, 0)
            tuple_b = (tuple_b[0], tuple_b[1]
        if len(tuple_a) == 2 and tuple_b == ():
            tuple_a = (tuple_a[0], tuple_a[1])
            tuple_b = (0, 0)

        add1 = tuple_a[0] + tuple_b[0]
        add2 = tuple_a[1] + tuple_b[1]
        new_tup = (add1, add2)
    return(new_tup)
