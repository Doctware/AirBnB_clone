#!/usr/bin/python3
""" this module contans the Entry point of the command interpriter """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    """
    The command interpriter
    1. Implementing EOF, quit, and help
    """
    def do_quit(self, arg):
        """Quit Command to exit the program """
        return True

    def do_EOF(self, arg):
        """EOF Command to exit the program """
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
