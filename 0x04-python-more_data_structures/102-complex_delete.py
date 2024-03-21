#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Delete all keys with values matching a given value """
    if a_dictionary:
        for k, v in list(a_dictionary.items()):
            if v == value:
                del a_dictionary[k]
        return a_dictionary
