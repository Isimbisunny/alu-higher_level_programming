#!/usr/bin/python3
"""Rename the state with identifier two to New Mexico."""
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
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()
    engine.dispose()
