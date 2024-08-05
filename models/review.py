#!/usr/bin/python

"""
A module that creates Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Create a Review class"""
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
