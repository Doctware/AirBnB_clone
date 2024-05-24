#!/usr/bin/python3
""" this module contain class HBNBCommand class """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """ Create: this command create instance of BaseModel
            save it to (the JSON file) and print the id
            Ex: $ create BaseModel """

        class_name = arg.strip() # Remove leading/trailing white spase

        if not class_name:
            print("** class name missing **")
        else:
            try:
                class_obj = {"BaseModel": BaseModel}
                if class_name not in class_obj:
                    raise KeyError("** class dosen't exist **")

                new_obj = class_obj[class_name]()
                storage.new(new_obj)
                storage.save()
                print("{}".format(new_obj.id))
            except KeyError as e:
                print(e)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
