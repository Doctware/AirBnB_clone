#!/usr/bin/python3
"""  This module contains the base class
    thats defines all common attributs/imethod for other classes"""
import uuid
import datetime


class BaseModel:
    """ The class BaseModel thats future classs
        inherit from """
    def __init__(self):
        """ the init method
            assign uniqe id to public instace attribute 'id'

            assign current datetime to public instance atribute 'created_at'
            assign current datetime to public instance atribute 'updated_at'
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Print BaseModel information according to formati"""
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
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()

        return to_dict
