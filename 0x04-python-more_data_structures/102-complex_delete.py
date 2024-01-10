#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for g, h in tmp.items():
        if value == h:
            my_dict.pop(g)
            return my_dict

