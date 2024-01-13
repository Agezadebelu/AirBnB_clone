#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityModel(unittest.TestCase):
    """Unit tests for the Amenity model."""

    def setUp(self):
        """Set up an Amenity instance for testing."""
        self.amenity = Amenity()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test if the Amenity class inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
