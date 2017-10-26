import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#create table cook contains all cook's info
class requestInfoRecord(Base):
    __tablename__ = 'requestInfo'

    id = Column(Integer, primary_key=True)
    location = Column(String(80))
    time = Column(String(80))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'location': self.location,
            'time': self.time,
            'id': self.id,
        }





engine = create_engine('sqlite:///CookMenu.db')


Base.metadata.create_all(engine)
