#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            if not new_list[i] == True:
                new_list[i] = True
        else:
            if new_list[i] == True:
                new_list[i] = False
    return new_list
