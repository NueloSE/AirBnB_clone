#!/usr/bin/python

"""
A module that creates a City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Create a class for city"""
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
