#!/usr/bin/python3
"""Module contains a script that will list states in a MySQL database"""
import MySQLdb
from sys import argv


def my_safe_filter_states():
    """Takes in an argument and displays all values in
    the states table wher the argument is matchd"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )

    cursor = db.cursor()
    name = argv[4]
    cursor.execute("SELECT * FROM states "
                   "WHERE BINARY name = %s "
                   "ORDER BY id", (name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
