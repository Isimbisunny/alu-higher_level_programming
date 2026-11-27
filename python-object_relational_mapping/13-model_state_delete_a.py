#!/usr/bin/python3
"""Delete states whose names contain the letter a."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    url = URL.create("mysql+mysqldb", username=sys.argv[1],
                     password=sys.argv[2], host="localhost",
                     port=3306, database=sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.contains("a"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
    engine.dispose()
