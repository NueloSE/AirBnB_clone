#!/usr/bin/python3
"""Module for define console actions"""

from models import storage
from models.base_model import BaseModel
from models.user import User



class Actions:
    """Help handling some console actions"""
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
    }

    @staticmethod
    def class_exists(class_name):
        """Checks if a class name is exists"""
        classes = Actions.__classes.keys()
        return class_name in set(classes)

    @staticmethod
    def valid_arguments(arg):
        """Check if the argument is valid"""
        if not arg:
            print("** class name missing **")
            return False

        k_class = arg[0]
        if not Actions.class_exists(k_class):
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def create(arg):
        """Create a new instance of class @arg[0]"""
        if not Actions.valid_arguments(arg):
            return

        k_class = arg[0]
        obj = Actions.__classes[k_class]()
        obj.save()
        print(obj.id)

    @staticmethod
    def tuple2value(arg, idx):
        """Returns the value of tuple, or None"""
        if len(arg) < idx + 1:
            return None
        return arg[idx]

    @staticmethod
    def object_exists(arg):
        """Check if the id is a valid object id"""
        id_obj = Actions.tuple2value(arg, 1)
        if not id_obj:
            print("** instance id missing **")
            return

        obj = storage.get_object(arg[0], id_obj)
        if obj is None:
            print("** no instance found **")
            return None

        return obj

    @staticmethod
    def show(arg):
        """Prins the string representation of an instance"""
        if not Actions.valid_arguments(arg):
            return

        obj = Actions.object_exists(arg)
        if not obj:
            return

        print(obj)

    @staticmethod
    def all(arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            print(storage.get_objects())
            return

        class_name = arg[0]
        if not Actions.class_exists(class_name):
            print("** class doesn't exist **")
            return

        print(storage.get_objects(class_name))

    @staticmethod
    def destory(arg):
        """Delete an instance based on the class name and id"""
        if not Actions.valid_arguments(arg):
            return
        obj = Actions.object_exists(arg)
        if not obj:
            return

        storage.delete(arg[0], arg[1])
        storage.save()

    @staticmethod
    def update(arg):
        if not Actions.valid_arguments(arg):
            return

        obj = Actions.object_exists(arg)
        if not obj:
            return

        attribute = Actions.tuple2value(arg, 2)
        if not attribute:
            print('** attribute name missing **')
            return

        value = Actions.tuple2value(arg, 3)
        if not value:
            print('** value missing **')
            return

        type_cast = type(attribute).__name__
        value = eval('{}(value)'.format(type_cast))
        setattr(obj, attribute, value)

        storage.save()
