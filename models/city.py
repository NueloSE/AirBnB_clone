#!/usr/bin/python

"""
A module that creates a City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Create a class for city"""
    state_id = ""
    name = ""
