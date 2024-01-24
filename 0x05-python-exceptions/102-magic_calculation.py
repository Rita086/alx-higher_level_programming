#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for l in range(1, 3):
        try:
            if l > a:
                raise Exception('Too far')
            result += a ** b / l
        except Exception:
            result = b + a
            break
    return result
