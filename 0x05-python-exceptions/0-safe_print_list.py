#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    counter = 0
    for i in my_list:
        leng += 1
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except:
            print("")
            return leng
        counter += 1
    print("")
    return counter
