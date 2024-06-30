#!/usr/bin/python
"""
A module that creates a class user which inherits from Basemodel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseMOdel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
