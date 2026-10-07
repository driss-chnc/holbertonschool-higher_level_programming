#!/usr/bin/python3
"""List states matching an argument from a MySQL database."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
