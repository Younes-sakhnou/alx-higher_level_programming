#!/usr/bin/python3
for num in range(0, 100):
    if (num >= 0) and (num <= 9):
        print("0{0:d}, ".format(num), end='')
    elif (num > 9) and (num <= 98):
        print("{0:d}, ".format(num), end='')
    else:
        print("{0:d} ".format(num), end='\n')
