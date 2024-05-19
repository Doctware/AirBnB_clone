#!/usr/bin/env python3
"""  This module contains the base class
    thats defines all common attributs/imethod for other classes"""
import uuid
import datetime


class BaseModel:
    """ The class BaseModel """
    def __init__(self):
        """ the init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Print BaseModel information """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute updated_at
            with the current datetime """
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns the dictionary contaning
            all key/value os __dict__ of instance """

        to_dict = self.__dict__.copy()

        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.datetime.datetime.isoformat()
        to_dict['updated_at'] = self.datetime.datetime.isoformat()

        return to_dict
