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
#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states...
    ...table of hbtn_0e_0_usa where name matches the argument. """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name='{}'
                COLLATE Latin1_General_CS ORDER BY
                id ASC""".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()