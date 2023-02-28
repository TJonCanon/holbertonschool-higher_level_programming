#!/usr/bin/python3
"""lists all State objs that have the given name in db"""
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
    found = session.query(State).filter(State.name == argv[4]).first()
    print(found.id if found else "Not found")
    session.close()
