#!/usr/bin/python3
""" lists all states starting with the letter N """
import MySQLdb
from sys import argv


if __name__=='_main__':
    db = MySQLdb.connect(user= argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id"
    )
    for state in cur.fetchall():
        print(state)
  