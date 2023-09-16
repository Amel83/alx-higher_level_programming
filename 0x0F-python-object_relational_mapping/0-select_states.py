#!/usr/bin/python3
"""  lists all states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbc=sys.argv[3], port=3306)
    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states")
    r = cursor.fetchall()
    for row in r:
        print(r)
    cursor.close()
    dbc.close()
