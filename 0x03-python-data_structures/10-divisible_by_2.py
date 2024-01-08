#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    current_list = []

    if my_list:

        for numb in my_list:

            current_list.append(False if numb % 2 else True)

        return current_list
