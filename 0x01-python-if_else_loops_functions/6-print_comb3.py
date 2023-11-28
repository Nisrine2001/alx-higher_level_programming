#!/usr/bin/python3
for num in range(0, 10):
    for digit in range(num + 1, 10):
        if num < digit:
            print("{:d}{:d}".format(num, digit),
                    end='\n' if num == 8 and digit == 9 else ", ")
