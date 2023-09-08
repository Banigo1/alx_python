#!/usr/bin/python3
"""List all State objects that contain the letter 'a' from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password>
              <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a MySQL database connection
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(db_url)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for State objects containing 'a' and sort by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')
                                                ).order_by(State.id)

    # Print the results in the specified format
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

