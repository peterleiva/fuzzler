#!/usr/bin/env python3

badchars = []

for num in range(1, 256):
    print(f"\\x{hex(num)}", end="")