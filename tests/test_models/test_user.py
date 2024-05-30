#!/usr/bin/python3
""" this module contains test port for User """
from models.user import User
import unittest
import uuid
from datetime import datetime


class UserTestCase(unittest.TestCase):
    """ the class UserTestCase """

    def setUp(self):
        """ the setup method """
        self.us = User()

    def test_use_instance(self):
        """ testing user instance """
        self.assertIsInstance(self.us, User)

    def test_user_attribute(self):
        """ testing user attribute """
        self.assertEqual(self.us.last_name, "")
        self.assertEqual(self.us.first_name, "")
        self.assertEqual(self.us.email, "")
        self.assertEqual(self.us.password, "")

    def test_user_id(self):
        """ testing user id """
        self.assertIsInstance(self.us.id, str)
        self.assertTrue(len(self.us.id) > 0)

    def test_user_created_at_updated_at(self):
        """ testing user created_at and updated_at attr """
        self.assertIsInstance(self.us.created_at, datetime)
        self.assertIsInstance(self.us.created_at, datetime)

    def test_user_str(self):
        """ testing __str__ method user """
        string = str(self.us)
        self.assertIn("[User] ({})".format(self.us.id), string)
        self.assertIn("'id': '{}'".format(self.us.id), string)

    def test_user_to_dict(self):
        """ testing dic method for user """
        us_dict = self.us.to_dict()
        self.assertEqual(us_dict[__class__], User)
        self.assertEqual(us_dict['last_name'], "")
        self.assertEqual(us_dict['first_name'], "")
        self.assertEqual(us_dict['email'], "")
        self.assertEqual(us_dict['password'], "")
        self.assertIsInstance(us_dict['created-at'], str)
        self.assertIsInstance(us_dict['Updated_at'], str)
        self.assertEqual(to_dict['created_at'], self.us.datetime.isoformat())
        self.assertEqual(to_dict['updated_at'], self.us.datetime.isoformat())


if __name__ == "__main__":
    unittest.main()
