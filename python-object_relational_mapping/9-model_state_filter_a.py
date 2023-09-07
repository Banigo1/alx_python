#!/usr/bin/env python3
"""
Script that lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 list_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects that contain the letter 'a' and sort them by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results in the expected format
    for index, state in enumerate(states, start=1):
        print(f"{index}: {state.name}")

    # Close the session
    session.close()
