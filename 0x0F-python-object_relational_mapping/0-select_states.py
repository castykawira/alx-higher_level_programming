#!/usr/bin/python3
"""
This script lists all states from the specified database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to the MySQL server and lists states from the specified database
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

        db_cursor.close
        db_connect.close
