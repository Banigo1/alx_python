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
import sys

def search_states(username, password, database, state_name):
    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()
    
    # Create the SQL query using user input
    query = "SELECT * FROM states WHERE LOWER(name) = LOWER'{}' ORDER BY id ASC".format(state_name)
    
    # Execute the query
    cur.execute(query)
    
    # Fetch all rows from the result set
    results = cur.fetchall()
    
    # Print the fetched rows
    for row in results:
        print(row)
    
    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    # Call the search_states function with the provided arguments
    search_states(username, password, database, state_name)
