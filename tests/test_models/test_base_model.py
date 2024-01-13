#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_string_representation(self):
        """Test if the __str__ method produces the correct string."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def tearDown(self):
        """Clean up resources after each test."""
        time.sleep(0.1)

    def test_save(self):
        """Test if the save method updates the 'updated_at' attribute."""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test if the to_dict method returns a dictionary with the correct keys."""
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_inheritance(self):
        """Test if the BaseModel class inherits from object."""
        self.assertTrue(issubclass(BaseModel, object))


if __name__ == '__main__':
    unittest.main()
