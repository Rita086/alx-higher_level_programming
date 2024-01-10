#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    c = sorted(a_dictionary)
    for i in c:
        print("{}: {}".format(i, a_dictionary[i]))
