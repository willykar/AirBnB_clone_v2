#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models


class Place(BaseModel, Base):
    """ This class Place
    Attributes:
        city_id: string
        user_id: string
        name: string
        description: string
        number_rooms: integer
        number_bathrooms: integer
        max_guest: integer
        price_by_night: integer
        lattitude: integer
        longitude: float
    """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
