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
        instance = '{}(**info)'.format(class_obj)
        return eval(instance)

    @staticmethod
    def delete(class_name, id):
        key = "{}.{}".format(class_name, id)
        del FileStorage.__objects[key]

    @staticmethod
    def get_object(class_name, id):
        """Get the key of an object by id"""
        key = '{}.{}'.format(class_name, id)
        return FileStorage.__objects.get(key, None)

    @staticmethod
    def get_objects(class_name=None):
        """Gets all objects"""
        objects = []
        for _, val in FileStorage.__objects.items():
            str_rep = str(val)
            if not class_name:
                objects.append(str_rep)
                continue

            if type(val).__name__ == class_name:
                objects.append(str_rep)

        return objects

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
