#!/usr/bin/python3
""" this module contains the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ the class user thats inherits from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
