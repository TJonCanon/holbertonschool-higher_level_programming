#!/usr/bin/python3
"""adds State obj Louisiana to db"""
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
    OperatorPutMeOnThru = State(name="Louisiana")
    session.add(OperatorPutMeOnThru)
    session.commit()
    print(OperatorPutMeOnThru.id)
    session.close()
