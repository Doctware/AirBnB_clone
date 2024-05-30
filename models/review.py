#!/usr/bin/python3
""" this module contains the class Review That inherit from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ The class Reveiw """

    place_id = ""
    user_id = ""
    text = ""
