#!/usr/bin/python3
"""adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        exit('Use: 11-model_state_insert.py <mysql username> '
             '<mysql password> <database name> ')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)  # creates decprecated warning
    session = Session(engine)

    new_state = State(name='Louisiana')
    session.add(new_state)  # 'pending', not added to db yet
    session.commit()

    print(new_state.id)
    session.close()
