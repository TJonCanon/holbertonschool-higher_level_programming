#!/usr/bin/python3
""" Take 10 """
import requests
from sys import argv


def main():
    print(requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
                  .json()
                  .get('id')
          )


if __name__ == "__main__":
    main()
