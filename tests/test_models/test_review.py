#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewModel(unittest.TestCase):
    """Unit tests for the Review model."""

    def setUp(self):
        """Set up a Review instance for testing."""
        self.review = Review()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test if the Review class inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
