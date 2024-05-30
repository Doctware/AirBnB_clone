#!/usr/bin/python3
""" This module contains the Class FileStorage  """
import json
from models.base_model import BaseModel
from models.user import User


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
        with open(__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self) -> None:
        """ method thats diserialze obj """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for obj_dict in data:
                    new_obj = BaseModel(**obj_dict)
                    self.__objects[f"{new_obj.__class__.__name__}.{new_obj.id}"] = new_obj
        except FileNotFoundError:
            pass
