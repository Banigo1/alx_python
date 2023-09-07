#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all...
    ...cities of that state, using the database hbtn_0e_4_usa """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities JOIN states ON cities.state_id =
                states.id WHERE states.name = %s ORDER BY cities.id ASC""",
                (argv[4],))
    query_rows = cur.fetchall()
    cities_print = []
    for row in query_rows:
        if row[4] == argv[4]:  # if state matches argv[4]
            cities_print.append(row[2])  # append the city to list cities_print
    print(', '.join(cities_print))  # output format desired by task description
    cur.close()
    conn.close()
# row 2 of normal output is cities
# row 4 of normal output is states
