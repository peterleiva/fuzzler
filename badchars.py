#!/usr/bin/env python3


def generate_badchars(low = 1, high = 256):
    badchars = []

    for num in range(low, high):
        badchars.append(hex(num).replace("0x", "\\x"))
        
    return badchars


if __name__ == "__main__":
    for char in generate_badchars():
        print(char, end="")
