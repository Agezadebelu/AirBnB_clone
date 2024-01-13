import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Set up a FileStorage instance for testing."""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test the new method."""
        user = User()
        self.storage.new(user)
        objects = self.storage.all()
        self.assertIn('User.{}'.format(user.id), objects)

    def test_save_and_reload(self):
        """Test the save and reload methods."""
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Create a new FileStorage instance to simulate a program restart
        new_file_storage = FileStorage()
        new_file_storage.reload()

        objects = new_file_storage.all()
        self.assertIn('User.{}'.format(user.id), objects)

    def test_attributes(self):
        """Test the attributes method."""
        attributes = self.storage.attributes()
        self.assertIsInstance(attributes, dict)


if __name__ == '__main__':
    unittest.main()
