#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel. Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlachemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """class Amenity
    attribute:
        name
        place_amenities

    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = Table('place_amenities', Base.metadata,
                            Column('place_id', String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True),
                            Column('amenity_id', String(60)
                                   ForeignKey('amenities.id'),
                                   primary_key=True))
    places = relationship("Place", secondary=place_amenities,
                          back_populates="amenities")
