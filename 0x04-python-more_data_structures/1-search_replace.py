#!/usr/bin/python3
def search_replace(my_list, search, replace):
    b_list = list(my_list)
    for i in range(len(b_list)):
        if b_list[i] == search:
            b_list[i] = replace
            return b_list
