from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, cook, MenuItem
from addTable import Customer

engine = create_engine('sqlite:///CookMenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Read information in database
all_cook = session.query(cook).all()
for i in all_cook:
    print(i.name)

items = session.query(MenuItem).all()
for i in items:
    print(i.name)

customers = session.query(Customer).all()
for i in customers:
    print(i.name)
