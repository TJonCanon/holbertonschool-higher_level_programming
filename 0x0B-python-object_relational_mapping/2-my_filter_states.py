#!/usr/bin/python3
"""Module contains a script that will list states in a MySQL database"""
import MySQLdb
from sys import argv


def my_filter_states():
    """Takes in an argument and displays all values inthe states table """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name = '{}' "
                "ORDER BY id".format(argv[4])
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_filter_states()
