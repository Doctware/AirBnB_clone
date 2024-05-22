#!/usr/bin/python3
""" this module contain class HBNBCommand class """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The Class HBNBCommnand class thats inherits from
        The Cmd Class
        To implement simple command interpreter for the HBNB project
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        print("Exiting HBNB command interpreter")
        print()
        exit()

    def do_EOF(self, arg):
        """ Exit the command interpreter on EOF (Ctrl-D)."""
        print()
        exit()

    def emptyline(self):
        """ Handle empty line input (just ENTER)."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
