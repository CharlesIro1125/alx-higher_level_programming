#!/usr/bin/python3
"""
connect to a db using MySQLdb "
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ select all states """

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM states s JOIN \
                cities c ON s.id=c.state_id ORDER BY c.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
