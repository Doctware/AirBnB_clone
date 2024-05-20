#!/usr/bin/python3
""" Test port for the BaseModel """
from models.base_model import BaseModel
from datetime import datetime
from unittest import TestCase
import uuid


class TestBaseModel(TestCase):
    """ The class TestBaseModel to test the BaseModel """

    def setUp(self):
        self.bm = BaseModel()
        self.bm.name = "My First Model"
        self.bm.number = 89

    def test_PubIstAtt(self):
        """ this method is testing the public insatnce attribute """
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_save(self):
        """ this method is testing the save method """
        original_created_at = self.bm.created_at
        self.bm.save()
        self.assertGreater(self.bm.updated_at, original_created_at)

    def test_to_dict(self):
        """ this method is testing to_dict method """
        data = self.bm.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        self.assertIn('created_at', data)
        self.assertIsInstance(data['created_at'], str)
        self.assertIn('updated_at', data)
        self.assertIsInstance(data['updated_at'], str)
        self.assertIn('__class__', data)
        self.assertEqual(data['__class__'], self.bm.__class__.__name__)
        self.assertEqual(data['name'], 'My First Model')
        self.assertEqual(data['number'], 89)

    def test_str(self):
        """ this method test string output """
        output = "[BaseModel] ({}) {}".\
            format(self.bm.id, self.bm.__dict__)
        self.assertEqual(str(self.bm), output)


if __name__ == "__main__":
    unittest.main()
