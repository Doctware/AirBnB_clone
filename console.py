#!/usr/bin/python3
""" this moduule contains the class HBNBcommand for cmd interpriter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""

        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""

        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not args or args == obj.__class__.__name__:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr = arg_list[2]
        value = arg_list[3].strip('"')
        setattr(obj, attr, value)
        obj.save()

    def emptyline(self):
        """Do nothing on empty line input"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
