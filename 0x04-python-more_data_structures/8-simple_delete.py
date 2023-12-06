#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

        my_dict = {"a": 1, "b": 2, "c": 3}
        simple_delete(my_dict, "b")
        print(my_dict) 
