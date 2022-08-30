#!/usr/bin/python3

def no_c(my_string):
    if len(my_string) < 1:
        return (None)
    copy_str = [x for x in my_string if x != 'c' or x != 'C' else pass]
    return ("".join(copy_str))
