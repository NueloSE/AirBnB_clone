#!/usr/bin/python

"""
A module that creates Review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
	place_id = ""
	user_id = ""
	text = ""
