#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Output the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements outputed.
    """
    num = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
