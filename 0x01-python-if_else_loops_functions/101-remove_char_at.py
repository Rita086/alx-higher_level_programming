#!/usr/bin/python3
def remove_char_at(str, e):
if e < 0:
return (str)
return (str[:e] + str[e+1:])
