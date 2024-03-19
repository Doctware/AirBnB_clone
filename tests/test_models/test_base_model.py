#!/usr/bin/python3
""" this module contains tests port for the base_model """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ the testbasemodel class """
    def setUp(self):
        """ Set up instance for base model """
        self.baseM = BaseModel()

    def test_init(self):
        """
        testing insialization of BaseModel
        """
        self.assertIsInstance(self.baseM.id, str)
        self.assertIsInstance(self.baseM.created_at, datetime)
        self.assertIsInstance(self.baseM.updated_at, datetime)

    def test_save(self):
        """ testing save method """
        oldUpdate = self.baseM.updated_at
        self.baseM.save()
        self.assertNotEqual(self.baseM.updated_at, oldUpdate)

    def test_to_dict(self):
        """ testing tO_dict method """
        O_dict = self.baseM.to_dict()
        self.assertIsInstance(O_dict, dict)
        self.assertIn('__class__', O_dict)
        self.assertEqual(O_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', O_dict)
        self.assertEqual(O_dict['created_at'], self.baseM.created_at.isoformat())
        self.assertIn('updated_at', O_dict)
        self.assertEqual(O_dict['updated_at'], self.baseM.updated_at.isoformat())

    def test_str(self):
        """ Testing __str__ method """
        output = "[BaseModel] ({}) {}".\
            format(self.baseM.id, self.baseM.__dict__)
        self.assertEqual(str(self.baseM), output)

if __name__ == "__main__":
    unittest.main()
