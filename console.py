#!/usr/bin/python3
"""
Model for instantiating console
"""
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
import shlex

classes = {
        'Amenity': Amenity,
        'BaseModel': BaseModel,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User,
}


class HBNBCommand(cmd.Cmd):
    """The command line module"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Helps to implement the end of line function\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Handle empty line when is passed as an argument"""
        pass

    do_exit = do_quit

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        if len(args) > 1:
            if args[0] in classes:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        args = shlex.split(arg)
        result = []
        if len(args) == 0:
            obj_item = models.storage.all()
        elif args[0] in classes:
            obj_item = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exit **")
            return False
        for item in obj_item:
            result.append(str(obj_item[item]))
        print(result)

    def do_update(self, arg):
        args = shlex.split(arg)
        arg_len = len(args)
        if arg_len == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if arg_len > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if arg_len > 2:
                        if arg_len > 3:
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def default(self, line):
        command, _, subcommand = line.partition('.')
        result = []
        if command in classes:
            for key in models.storage.all():
                if key.split('.')[0] == command:
                    result.append(str((models.storage.all()[key])))
            if subcommand == "all()":
                print(result)
            elif subcommand == "count()":
                print(len(result))
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
