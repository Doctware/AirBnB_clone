#!/usr/bin/python3
""" this module contains the class City thats inherit from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ The class City """
    state_id = ""
    name = ""
