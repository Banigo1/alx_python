#!/usr/bin/python3

""" 
This script uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
It takes four arguments:

    mysql username,
    mysql password,
    database name, and
    state name searched. 

The script is safe from MySQL injections because it uses parameterized queries to pass the state name to the SELECT statement.

The results are sorted in ascending order by states.id.

The code is not executed when imported because it is placed inside an 
if __name__ == "__main__": block.

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
