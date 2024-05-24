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

        class_name = arg.strip()

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

    def do_show(self, arg):
        """
        print the string representation of an instance base on
        class name and id. Ex: ($: show BaseModel 1234-1234-1234)
        """

        args = arg.strip().split()  # split argument by white space

        if not args:
            print("** class name missing **")
        else:
            class_name, obj_id = args[0], None

            if len(args) > 1:
                obj_id = args[1]

            try:
                if not class_name:
                    raise ValueError("** class name missing **")
                if not obj_id:
                    raise ValueError("** obj_id missing **")

                obj = storage.all()
                if not obj:
                    raise ValueError("** no instance found **")

                print(obj)
            except ValueError as e:
                print(e)

    def do_destroy(self, arg):
        """ delete an instance base on class name and id
            then save the changes into a json file
            Ex: ($: destroy BaseModel 1234-1234-1234)
        """

        args = arg.strip().split()

        if not args:
            print("** class name missing **")
        else:
            class_name, obj_id = args[0], None
            if len(args) > 1:
                obj_id = args[1]
            try:
                if not class_name:
                    raise ValueError("** class name missing **")
                if not obj_id:
                    raise ValueError("** instance id missing **")

                obj = storage.all()
                if not obj:
                    raise ValueError("** no instance found **")

                del obj
                storage.save()

            except ValueError as e:
                print(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
