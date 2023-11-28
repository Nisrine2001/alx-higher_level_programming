#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for num, c in enumerate(str):
        if num != n:
            new_string += c
        return new_string
