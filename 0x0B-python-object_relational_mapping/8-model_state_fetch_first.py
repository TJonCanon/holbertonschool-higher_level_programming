#!/usr/bin/python3
"""lists first State obj in db"""
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
    state = session.query(State).order_by(State.id).first()
    print("Nothing" if state is None else f"{state.id}: {state.name}")
    session.close()
