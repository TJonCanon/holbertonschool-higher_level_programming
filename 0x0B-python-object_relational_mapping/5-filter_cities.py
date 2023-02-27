#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id WHERE states.name=%s \
                ORDER BY cities.id ASC", (state_name,))
    rows = cursor.fetchall()
    if cities is not None:
        print(", ".join(city[0] for city in cities))
    cursor.close()
    db.close()