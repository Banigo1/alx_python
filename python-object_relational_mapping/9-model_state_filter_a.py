#!/usr/bin/python3
"""
Script to list all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_letter_a(username, password, database_name):
    """List all State objects containing the letter 'a'"""
    # Create a database connection using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database_name))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to find State objects containing the letter 'a'
    # and order by states.id
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} <username> <password> <database_name>'.format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_letter_a(username, password, database_name)
