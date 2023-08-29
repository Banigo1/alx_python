#!/usr/bin/python3

"""
This script uses MySQLdb module (import MySQLdb),
takes 4 arguments:

    mysql username,
    mysql password,
    database name and
    state name searched (safe from MySQL injection),
    
connects to a MySQL server running on localhost at port 3306,
Sorts result in ascending order by states.id, and prints name
and id safety for given name for a table using MySQLdb

"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    
    
    cur = db.cursor()
    
    
    cur.execute("SELECT DISTINCT id,\
                name FROM states WHERE name = %s\
                ORDER BY id ASC", [sys.argv[4]])

    rows = cur.fetchall()
    
    
    for r in rows:
        
        
        print(r)