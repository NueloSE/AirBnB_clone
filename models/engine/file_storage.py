#!/usr/bin/python3
"""
Module for handling storage with a file
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serialization of instances to a Json file and deserialize Json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Updates the __objects dictionary with a new instance
        """
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves __object to the file storage
        """
        json_data = {}
        for key, val in FileStorage.__objects.items():
            json_data[key] = val.to_dict()
        
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(json_data, file)

    @staticmethod
    def create_object(info):
        """
        returns an update of an instance
        """
        class_obj = info['__class__']
        instance ='{}(**info)'.format(class_obj)
        return eval(instance)

    def reload(self):
        """
        Loads the instances stored in the storage file to the __object
        """
        filename = FileStorage.__file_path

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                dict_data = json.load(f)

            for key, val in dict_data.items():
                obj = FileStorage.create_object(val)
                FileStorage.__objects[key] = obj
