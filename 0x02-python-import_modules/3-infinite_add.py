#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition = 0
    for num in range(len(sys.argv) - 1):
        addition += int(sys.argv[num + 1])
    print(addition)
