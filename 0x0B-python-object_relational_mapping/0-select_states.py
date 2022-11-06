#!/usr/bin/python3
""" list al states from database 'hbtn_0e_usa' """

import MySQLdb

def print_state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3006, user=argv[1],
                        password=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()


if __name__=="__main__":
    print_state()
