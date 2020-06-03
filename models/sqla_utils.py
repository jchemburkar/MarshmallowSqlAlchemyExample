''' utils for maintaining database with sqlalchemy '''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


ENGINE = create_engine('mysql+pymysql://root:@localhost/nhl', echo=False)
BASE = declarative_base(bind=ENGINE)


def get_session():
    '''
    gets a sqlalchemy session -- useful for interfacing with the database
    Docs: https://docs.sqlalchemy.org/en/13/orm/session.html
    '''
    return Session(bind=ENGINE)
