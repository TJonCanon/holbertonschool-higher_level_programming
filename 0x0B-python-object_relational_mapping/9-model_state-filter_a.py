#!/usr/bin/python3
"""lists all State objs that contain letter a in db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    Session = sessionmaker(
        bind=create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]
            )
        )
    )
    session = Session()
    stAtes = session.query(State).filter(State.name.like("%a%"))
    for state in stAtes:
        print(f"{state.id}: {state.name}")
    session.close()