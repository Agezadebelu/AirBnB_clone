#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityModel(unittest.TestCase):
    """Unit tests for the City model."""

    def setUp(self):
        """Set up a City instance for testing."""
        self.city = City()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test if the City class inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
