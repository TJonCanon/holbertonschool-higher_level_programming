#!/usr/bin/python3
"""changes name of a State obj from db"""
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
    new = session.query(State).filter(State.id == '2').first()
    new.name = "New Mexico"
    session.commit()
    session.close()
