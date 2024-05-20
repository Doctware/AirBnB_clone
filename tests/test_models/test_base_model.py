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

    def test_PubIstAtt(self):
        """ this method is testing the public insatnce attribute """
        self.assertIsInstance(self.bm.id, str)
        self.assertEqual(len(self.bm.id), 36)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_save(self):
        """ this method is testing the save method """
        original_created_at = self.bm.created_at
        self.assertGreater(self.bm.updated_at, original_created_at)

    def test_to_dict(self):
        """ this method is testing to_dict method """
        data = self.bm.to_dict()
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
