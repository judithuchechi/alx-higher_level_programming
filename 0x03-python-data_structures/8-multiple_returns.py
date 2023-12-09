#!/usr/bin/python3

def multiple_returns(sentence):

    str_len = len(sentence)
    new_tup = ()

    if sentence == "":
        new_tup = (0, None)

    if str_len >= 1:
        new_tup = (str_len, sentence[0])
    return new_tup
