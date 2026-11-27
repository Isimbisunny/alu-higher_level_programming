#!/usr/bin/python3
"""List cities alongside their corresponding state names."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    url = URL.create("mysql+mysqldb", username=sys.argv[1],
                     password=sys.argv[2], host="localhost",
                     port=3306, database=sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    cities = session.query(State, City).join(City, State.id == City.state_id)
    for state, city in cities.order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
    engine.dispose()
