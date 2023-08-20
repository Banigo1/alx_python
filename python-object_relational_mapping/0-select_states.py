#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa
The script uses two modules: MySQLdb and sys.
MySQLdb is a Python interface to the MySQL database. It is used to connect to a MySQL database and execute 
SQL queries

"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
"""
MySQLdb.connect() method is used to establish a connection to the MySQL database. 

"""
conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=dbname,
                           charset="utf8")
cur = conn.cursor()

"""     
    The cursor.execute() method is used to execute an 
    SQL query that selects all rows from the states table 
    and orders them by the id column in ascending order.
"""

cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
        print(row)
cur.close()
conn.close()
    
    
    