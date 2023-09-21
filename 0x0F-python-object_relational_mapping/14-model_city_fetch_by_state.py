#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
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
        # Query all City objects sorted by city id
        cities = session.query(City).order_by(City.id).all()

        # Print the results
        for city in cities:
            state_name = session.query(State).filter(State.id == city.state_id).first().name
            print("{}: ({}) {}".format(state_name, city.id, city.name))
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()
