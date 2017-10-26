import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#create table cook contains all cook's info
class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    location = Column(String(80))
    time = Column(String(80))
    card = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'location': self.location,
            'time': self.time,
            'card': self.card,
            'id': self.id,
        }





engine = create_engine('sqlite:///CookMenu.db')


Base.metadata.create_all(engine)
