#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states_with_a = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_with_a:
            session.delete(state)
        session.commit()
        print("{} state(s) deleted.".format(len(states_with_a)))
    except Exception as e:
        print("Error:", e)
        session.rollback()
    finally:
        session.close()
