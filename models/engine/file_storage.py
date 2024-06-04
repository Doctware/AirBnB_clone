#!/usr/bin/python3
""" This module contains the Class FileStorage  """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """ The class FileStorage
        were we serialized and diserialized"""
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """ this method returns dictonary __object """
        return self.__objects.copy()

    def new(self, obj) -> None:
        """ this method set in __object the obj with key
            <obj class name>.id """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """ this method is udes to serialized __objects the JSON file
            (paht: __file_path) """

        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self) -> None:
        """ method thats diserialze obj """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass
