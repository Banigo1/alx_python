#!/usr/bin/python3

"""
This script uses the MySQLdb module to connect
to a MySQL server running on localhost at port 3306.

It takes four arguments:

    mysql username,
    mysql password,
    database name, and
    state name searched.

The results are sorted in ascending order by states.id.

The script is safe from MySQL injections because it uses
parameterized queries to pass the state name to the SELECT statement.

A parameterized query is a type of SQL query in
which placeholders are used for parameters,
and the parameter values are supplied at execution time.

The main advantage of using parameterized queries is to avoid SQL
injection attacks. By using placeholders for parameters,
the query plan is constructed on the server before the query
is executed with parameter values.
This means that the structure of the query is fixed and
cannot be altered by user input, making it much more difficult
for an attacker to inject malicious code into the query.
Additionally, using parameterized queries can also improve performance,
as the database can cache the query plan and reuse it
for subsequent executions with different parameter values.


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

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cur = db.cursor()
    
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
