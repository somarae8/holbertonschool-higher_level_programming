#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return("None")
    else:
        n = 0
        for i in my_list:
            if i >= n:
                n = i
        return(n)
