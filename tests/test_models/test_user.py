#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserModel(unittest.TestCase):
    """Unit tests for the User model."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test if the User class inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
