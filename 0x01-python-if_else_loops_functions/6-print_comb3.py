#!/usr/bin/python3
a = 0
b = 0
for x in range(a, 9):
    for y in range(b, 10):
        if x != 8 or y != 9:
            print("{}{},".format(x, y), end=" ")
        else:
            print("{}{}".format(x, y))
    a = a + 1
    b = a + 1
