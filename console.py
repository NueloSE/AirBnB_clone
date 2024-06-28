#!/usr/bin/python3
"""
Model for instantiating console
"""
import cmd


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
        pass

    def postloop(self):
        print(end='')

    do_exit = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
