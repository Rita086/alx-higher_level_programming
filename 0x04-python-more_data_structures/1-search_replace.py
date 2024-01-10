#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(my_list)
    for b in range(len(n_list)):
    if n_list[b] == search:
    n_list[b] = replace
    return n_list
