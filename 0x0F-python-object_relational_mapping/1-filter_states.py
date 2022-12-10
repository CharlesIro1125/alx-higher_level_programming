#!/usr/bin/env python3
"""
connect to a db using MySQLdb "
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ select all states """

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE LEFT(UPPER(name), 1)
                IN('N',) ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()