#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the database
    Base.metadata.create_all(engine)

    # Create a Session class that will be used to interact with the database
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # You can perform database operations using the 'session' object

    # Close the session when done
    session.close()
