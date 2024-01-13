#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateModel(unittest.TestCase):
    """Unit tests for the State model."""

    def setUp(self):
        """Set up a State instance for testing."""
        self.state = State()

    def test_initialization(self):
        """Test if the instance variables are initialized correctly."""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test if the State class inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
