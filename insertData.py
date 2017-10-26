from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, cook, MenuItem

engine = create_engine('sqlite:///CookMenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Execute CRUB operation
#Add cook
Guangdong = cook(name = "Guangdong")
Hunan = cook(name = "Hunan")
session.add_all([Guangdong, Hunan])




# Add menu items
Mifen = MenuItem(name = 'Mifen', description = 'awesome breakfast', price = '6', cook = Hunan)
Youtiao = MenuItem(name = 'Youtiao', description = 'fried dough', price = '3', cook = Guangdong)
DouJiang = MenuItem(name = 'DouJiang', description = 'bean smoothie', price = '3', cook = Guangdong)
session.add_all([Mifen, Youtiao, DouJiang])

# Add customer
Su = Customer(name = 'Su', location = 'uw')
session.add(Su)

session.commit()
