import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def test_user_attributes(self):
        """Test that User class has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_to_dict(self):
        """Test that to_dict method includes all user attributes"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "yusclever9@gmail.com")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('id', user_dict)
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

