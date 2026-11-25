#!/usr/bin/python3
"""Additional tests for Rectangle constructor arguments."""
import unittest
from models.rectangle import Rectangle


class TestRectangleConstructor(unittest.TestCase):
    """Test rectangle construction with optional arguments."""

    def test_two_arguments(self):
        """Test construction with width and height only."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_three_arguments(self):
        """Test construction with width, height and x."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
