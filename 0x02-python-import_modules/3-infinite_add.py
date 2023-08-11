#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numer = len(sys.argv)
    sum = 0
    if numer > 1:
        for i in range(1, numer):
            sum += int(sys.argv[i])
        print("{}".format(sum))
    else:
        print("{}".format(sum))
