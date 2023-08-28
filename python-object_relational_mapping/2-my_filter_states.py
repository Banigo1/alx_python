#!/usr/bin/python3

""" LIKE TASK 2 BUT MORE SECURE, SO USE THIS WAY: 
""
This script takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
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
