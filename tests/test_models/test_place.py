#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceModel(unittest.TestCase):
    """Unit tests for the Place model."""

    def setUp(self):
        """Set up a Place instance for testing."""
        self.place = Place()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test if the Place class inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
