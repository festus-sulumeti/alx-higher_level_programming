#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    for num in my_list:
        if num not in my_list:
            my_list.append(num)
            sum += num
    return sum
