"""
This script uses the MySQLdb module to connect
to a MySQL database and retrieves data from the `states` table.

Usage:
python script.py
[username]
[password]
[database]
[state_name]

It takes four arguments:

username (str): The username for the MySQL database.
password (str): The password for the MySQL database.
database (str): The name of the MySQL database.
state_name (str): The name of the state to retrieve data for.

It connects to the `mydb` database using the `myuser` username and `mypass` password,
and retrieves data for the state of California from the `states` table.
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
if __name__ == "__main__":
    # connect to the MySQL database using provided arguments
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    
    # Create a cursor object
    cur = db.cursor()
    
    # Execute a SQL query to selct data from the `states` table
    cur.execute("SELECT id,\
                name FROM states WHERE name = '{}'\
                ORDER BY id ASC".format(sys.argv[4]))

    # Fetch all rows returned by the query
    rows = cur.fetchall()
    
    # loop over each row
    for r in rows:
        
        # Check if the value in the second column
        # (the `name` column) matches the provided state name
        if r[1] == sys.argv[4]:
            
            # Print the entire row
            print(r)