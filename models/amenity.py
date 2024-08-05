#!/usr/bin/python

"""
A module that creates Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Create a Amentity class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
