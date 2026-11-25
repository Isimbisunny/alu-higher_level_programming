#!/usr/bin/python3
"""Unit tests for the Square model."""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test square attributes and inherited methods."""

    def test_constructor(self):
        """Test inheritance and initial attributes."""
        s = Square(3, 1, 2, 4)
        self.assertIsInstance(s, Rectangle)
        self.assertEqual((s.size, s.width, s.height, s.id),
                         (3, 3, 3, 4))

    def test_size(self):
        """Test size updates and validation."""
        s = Square(2)
        s.size = 5
        self.assertEqual((s.width, s.height, s.size), (5, 5, 5))
        for value in ("2", 2.5, None, True):
            with self.assertRaisesRegex(
                    TypeError, "width must be an integer"):
                s.size = value
        for value in (0, -1):
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                s.size = value

    def test_area(self):
        """Test inherited area calculation."""
        self.assertEqual(Square(5).area(), 25)

    def test_display(self):
        """Test inherited display method."""
        output = StringIO()
        with redirect_stdout(output):
            Square(2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_str(self):
        """Test string representation."""
        self.assertEqual(str(Square(3, 1, 2, 4)),
                         "[Square] (4) 1/2 - 3")

    def test_update(self):
        """Test positional and keyword updates."""
        s = Square(1)
        s.update(10, 2, 3, 4, size=99)
        self.assertEqual(s.to_dictionary(),
                         dict(id=10, size=2, x=3, y=4))
        s.update(size=8, x=0, y=0, id=20)
        self.assertEqual(s.to_dictionary(),
                         dict(id=20, size=8, x=0, y=0))

    def test_dictionary(self):
        """Test dictionary representation."""
        self.assertEqual(Square(3, 1, 2, 4).to_dictionary(),
                         dict(id=4, size=3, x=1, y=2))
