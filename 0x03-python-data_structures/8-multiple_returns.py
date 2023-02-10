#!/usr/bin/python3

def multiple_returns(sentence):

    str_len = len(sentence)
    new_tup = ()
    first = sentence[0]

    if str_len == 0:
        new_tup = (str_len, 'None')
    else:
        new_tup = (str_len, first)
    return(new_tup)
