#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a Session class that will be used to interact with the database
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Query all State objects with their corresponding City objects
        states = session.query(State).order_by(State.id).all()

        # Loop through the states and their cities, and print the results
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()
