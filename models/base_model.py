#!/usr/bin/python3
"""
BaseModel module
This module contains the BaseModel class,
which defines common attributes and methods for other classes.
"""
import uuid
import datetime as dt


class BaseModel:
    """
    BaseModel class
    This class defines common attributes and methods for other classes.
    """
    def __init__(self, **kwargs):
        """
        Initializes a new BaseModel instance.
        Sets the id, created_at, and updated_at attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key  in ['created_at', 'updated_at']:
                        value = dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        Includes all instance attributes,
        with created_at and updated_at converted to ISO format strings.
        """
        ser_dict = self.__dict__
        ser_dict["__class__"] = self.__class__.__name__
        ser_dict['created_at'] = self.created_at.isoformat()
        ser_dict['updated_at'] = self.updated_at.isoformat()
        return ser_dict
