# Python - Object-relational mapping

 ## By: Guillaume, CTO at Holberton School
 
 ## Description
### From this project, I learnt:

* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script 
* How to map a Python Class to a MySQL table
* What ORM means
* Parameterized query 
## Background Context

In this project, MySQL server is in 8.1. I linked two amazing worlds: Databases and Python!
In the first part, the module MySQLdb connects to a MySQL database and execute your SQL queries.
In the second part, I used the module SQLAlchemy, an Object Relational Mapper (ORM).
The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t need to write any SQL queries only Python code. Last thing, code won’t be “storage type” dependent. 
and you will be able to change your storage easily without re-writing your entire project.

### Without ORM:

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

### With an ORM:

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()

Do you see the difference?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always.


# Projects

### [0. Get all states](./0-select_states.py)
* Write a script that lists all states from the database hbtn_0e_0_usa: 


### [1. Filter states](./1-filter_states.py)
* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: 


### [2. Filter states by user input](./2-my_filter_states.py)
* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.


### [3. SQL Injection...](./3-my_safe_filter_states.py)
* Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?


### [4. Cities by states](./4-cities_by_state.py)
* Write a script that lists all cities from the database hbtn_0e_4_usa 


### [5. All cities by state](./5-filter_cities.py)
* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa 

### [6. First state model](./model_state.py)
* 
### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)
* Write a script that lists all State objects from the database hbtn_0e_6_usa 

### [8. First state](./8-model_state_fetch_first.py)
* Write a script that prints the first State object from the database hbtn_0e_6_usa 

### [9. Contains `a`](./9-model_state_filter_a.py)
* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa 

## Author
*[Precious Banigo](https://github.com/banigo1)