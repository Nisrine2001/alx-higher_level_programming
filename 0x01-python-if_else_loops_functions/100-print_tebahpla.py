#!/usr/bin/python3
for alphabet in range(25, -1, -1):
    c = alphabet + ord('A')
    if alphabet % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
