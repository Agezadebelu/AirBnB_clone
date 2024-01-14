#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import unittest
import json
import os
from datetime import datetime
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path
        self.file_storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after the test."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method."""
        self.file_storage._FileStorage__objects = {}  # Clear objects
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.file_storage.all())

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        with open(self.file_path, 'w') as file:
            json.dump({"dummy": "data"}, file)  # Write a dummy object

        obj = BaseModel()
        obj_id = "BaseModel." + obj.id
        self.file_storage.new(obj)
        self.file_storage.save()

        with open(self.file_path, "r") as f:
            saved_data = json.load(f)
            self.assertIn(obj_id, saved_data)

        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path
        new_file_storage.reload()
        self.assertIn(obj_id, new_file_storage.all())

    def test_classes(self):
        """Test the classes() method."""
        classes = self.file_storage.classes()
        self.assertEqual(classes["BaseModel"], BaseModel)
        self.assertEqual(classes["User"], User)
        self.assertEqual(classes["State"], State)
        self.assertEqual(classes["City"], City)
        self.assertEqual(classes["Amenity"], Amenity)
        self.assertEqual(classes["Place"], Place)
        self.assertEqual(classes["Review"], Review)

    def test_reload_nonexistent_file(self):
        """Test the reload() method when the file does not exist."""
        if os.path.isfile(self.file_path):
            new_file_storage = FileStorage()
            new_file_storage._FileStorage__file_path = self.file_path
            new_file_storage.reload()
            self.assertEqual(new_file_storage.all(), {})

    def test_attributes(self):
        """Test the attributes() method."""
        attrs = self.file_storage.attributes()
        self.assertEqual(attrs["BaseModel"]["id"], str)
        self.assertEqual(attrs["User"]["email"], str)
        self.assertEqual(attrs["State"]["name"], str)
        self.assertEqual(attrs["City"]["state_id"], str)
        self.assertEqual(attrs["Amenity"]["name"], str)
        self.assertEqual(attrs["Place"]["city_id"], str)
        self.assertEqual(attrs["Review"]["place_id"], str)


if __name__ == '__main__':
    unittest.main()
