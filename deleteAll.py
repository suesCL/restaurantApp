from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, cook, MenuItem

engine = create_engine('sqlite:///CookMenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Mifen = session.query(MenuItem).filter_by(id = 7).one()
Youtiao = session.query(MenuItem).filter_by(id = 8).one()
DouJiang = session.query(MenuItem).filter_by(id = 9).one()

session.delete(Mifen)
session.delete(Youtiao)
session.delete(DouJiang)

session.commit()
