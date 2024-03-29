#!/usr/bin/python3
""" Task 8 """
import requests
from sys import argv


def main():
    q = "" if len(argv) == 1 else argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        r_dict = r.json()
        if r_dict.get('id') is None:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
