#!/usr/bin/python3
"""  lists all states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursorr = dbc.cursor()
    cursorr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    r = cursorr.fetchall()
    for row in r:
        print(r)
    cursorr.close()
    db.close()
