#!/usr/bin/python3
"""  This module contains the base class
    thats defines all common attributs/imethod for other classes """
import uuid
import datetime
import models


class BaseModel:
    """ The class BaseModel thats future classs
        inherit from """

    def __init__(self, *args, **kwargs):
        """ the init method
            assign uniqe id to public instace attribute 'id'

            assign current datetime to public instance atribute 'created_at'
            assign current datetime to public instance atribute 'updated_at'

            args: (Unused arguments)

            Using kwargs:
                check if kwargs is not empty if so....
                each key of this dictionary is an attribute name.
                each value of this dictionary is the value
                of the attribute name
        """

        # do this if kwargs is called
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Print BaseModel information according to formati"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns the dictionary contaning
            all key/value os __dict__ of instance """

        to_dict = self.__dict__.copy()

        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()

        return to_dict
