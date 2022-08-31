#!/usr/bin/python3
import string
for i in string.ascii_lowercase:
    if i in ["e", "q"]:
        continue
    print("{}".format(i), end="")
