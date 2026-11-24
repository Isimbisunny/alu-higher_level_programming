#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Return the max from an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Return the max from an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Return None for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_list(self):
        """Return the largest negative value."""
        self.assertEqual(max_integer([-1, -4, -2]), -1)


if __name__ == '__main__':
    unittest.main()
