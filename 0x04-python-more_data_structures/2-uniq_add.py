#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_dict = {}
    for num in my_list:
        if num not in uniq_dict:
            uniq_dict[num] = 0
            uniq_dict[num] += 1

            return sum(uniq_dict.values())
                                                
