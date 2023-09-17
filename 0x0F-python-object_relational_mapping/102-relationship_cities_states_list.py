#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa along with their corresponding State objects.
"""
import sys
from sqlalchemy import create_engine
from model_city import City
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            state_name = city.state.name
            print("{}: {} -> {}".format(city.id, city.name, state_name))
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()
