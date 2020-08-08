#!/usr/bin/python3
"""This module defines a class"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(username, password, database),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)
session = Session(bing=engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()

