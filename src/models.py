import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planets_favourites = relationship('Favourites_planets')
    characters_favourites = relationship('Favourites_characters')


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mass = Column(Float(250), nullable=False)
    population = Column(Integer(250), nullable=False)
    planets_favourites = relationship('Favourites_planets')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eyes_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    gender = Column(Boolean(), nullable=False)
    characters_favourites = relationship('Favourites_characters')
    
class Favourites_planets(Base):
    __tablename__ = 'favourites_planets'
    id = Column(Integer, primary_key=True)
    favourites_planets = Column(Integer, ForeignKey("planets.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id")) 

class favourites_characters(Base):
    __tablename__ = 'favourites_characters'
    id = Column(Integer, primary_key=True)
    favourites_characters = Column(Integer, ForeignKey("characters.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id")), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')