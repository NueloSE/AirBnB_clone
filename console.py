#!/usr/bin/python3
"""
Model for instantiating console
"""
import cmd
from actions import Actions


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

    def do_create(self, args):
        """Creates a new instance of the BaseModel"""
        args = HBNBCommand.parse_arg(args)
        Actions.create(args)

    def do_show(self, args):
        pass
        args = HBNBCommand.parse_arg(args)
        Actions.show(args)

    def do_destory(self, args):
        """Delete an instance based on the class name and id"""
        args = HBNBCommand.parse_arg(args)
        Actions.destory(args)

    def do_all(self, args):
        args = HBNBCommand.parse_arg(args)
        Actions.all(args)

    def do_update(self, args):
        args = HBNBCommand.parse_arg(args)
        Actions.update(args)

    @staticmethod
    def parse_arg(arg):
        """Convert any argument string into argument tuple"""
        return tuple(map(str, arg.split()))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
