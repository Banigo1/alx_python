#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the connection URL
    connection_url = f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'

    # Create the engine and session
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for State objects containing the letter 'a'
    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in query:
        print(f'{state.id}: {state.name}')

    # Close the session
    session.close()
