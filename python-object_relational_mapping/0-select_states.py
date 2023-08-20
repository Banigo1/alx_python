#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows
    rows = cur.fetchall()
    # Print the rows
    for row in rows:
        print(row)
    # Close the cursor and the connection to the database
    cur.close()
    db.close()