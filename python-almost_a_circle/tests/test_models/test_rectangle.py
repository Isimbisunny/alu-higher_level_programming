#!/usr/bin/python3
"""Unit tests for the Rectangle model."""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test rectangle attributes and methods."""

    def test_constructor(self):
        """Test inheritance and initial attributes."""
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertIsInstance(r, Base)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (2, 3, 4, 5, 6))

    def test_validation(self):
        """Test invalid constructor and setter values."""
        r = Rectangle(2, 3)
        for name in ("width", "height", "x", "y"):
            for value in ("2", 2.5, None, [], True):
                with self.assertRaisesRegex(
                        TypeError, name + " must be an integer"):
                    setattr(r, name, value)
            with self.assertRaises(ValueError):
                setattr(r, name, -1)
        for name in ("width", "height"):
            with self.assertRaises(ValueError):
                setattr(r, name, 0)
        with self.assertRaises(TypeError):
            Rectangle("2", 3)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_area(self):
        """Test area calculation."""
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_display(self):
        """Test display with and without offsets."""
        output = StringIO()
        with redirect_stdout(output):
            Rectangle(2, 2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")
        output = StringIO()
        with redirect_stdout(output):
            Rectangle(2, 2).display()
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_str(self):
        """Test string representation."""
        self.assertEqual(str(Rectangle(2, 3, 4, 5, 6)),
                         "[Rectangle] (6) 4/5 - 2/3")

    def test_update(self):
        """Test positional and keyword updates."""
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5, width=99)
        self.assertEqual(r.to_dictionary(),
                         dict(id=10, width=2, height=3, x=4, y=5))
        r.update(width=8, height=9, x=0, y=0, id=20)
        self.assertEqual(r.to_dictionary(),
                         dict(id=20, width=8, height=9, x=0, y=0))

    def test_dictionary(self):
        """Test dictionary representation."""
        self.assertEqual(Rectangle(2, 3, 4, 5, 6).to_dictionary(),
                         dict(id=6, width=2, height=3, x=4, y=5))
