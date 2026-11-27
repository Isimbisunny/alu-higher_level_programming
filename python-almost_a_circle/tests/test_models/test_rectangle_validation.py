#!/usr/bin/python3
"""Unit tests for Rectangle constructor validation."""
import unittest
from models.rectangle import Rectangle


class TestRectangleValidation(unittest.TestCase):
    """Verify constructor validation for all rectangle attributes."""

    def test_invalid_width_type(self):
        """Reject a string width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        """Reject a string height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_invalid_x_type(self):
        """Reject a string horizontal coordinate."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        """Reject a string vertical coordinate."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        """Reject a negative width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Reject a negative height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Reject a zero width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Reject a zero height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Reject a negative horizontal coordinate."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Reject a negative vertical coordinate."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)
