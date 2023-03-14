#!/usr/bin/python3
""" Task 3 """
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            print(resp.read().decode('utf8'))

    except error.HTTPError as err:
        print("Error code: {}".format(err.code))