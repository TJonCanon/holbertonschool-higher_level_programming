#!/usr/bin/python3
""" contains a script that will list states in a MySQL database """
import MySQLdb
from sys import argv


def filter_states():
    """ lists all states with a name starting with N """

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE BINARY name LIKE 'N%' "
                   "ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
