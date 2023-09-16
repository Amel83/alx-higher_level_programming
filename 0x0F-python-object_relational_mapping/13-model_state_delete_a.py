#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
        # Query and delete State objects with 'a' in their name
        states_with_a = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_with_a:
            session.delete(state)

        # Commit the changes to the database
        session.commit()
        print("{} state(s) deleted.".format(len(states_with_a)))
    except Exception as e:
        print("Error:", e)
        session.rollback()
    finally:
        # Close the session
        session.close()
