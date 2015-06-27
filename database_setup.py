# Configuration 1
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

#Class
class Restaurant(Base):
	#Table
    __tablename__ = 'restaurant'
   
    #Mappers
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250))
    city = Column(String(50))
    state = Column(String(50))
 
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(50), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(50))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
 
# Configuration 2
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)