#!/usr/bin/python3


def magic_calculation(q ,r):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if q < r:
        s = add(q, r)
        for j in range(4, 6):
            s = add(s, j)
        return (s)

    else:
        return(sub(q, r))
