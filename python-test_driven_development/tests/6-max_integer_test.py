#!/usr/bin/python3
"""Unit tests for the max_integer function."""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for finding the maximum integer in a list."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_all_negative(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)
        self.assertEqual(max_integer([0]), 0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_duplicates(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_zero(self):
        self.assertEqual(max_integer([-5, 0, -2]), 0)


if __name__ == "__main__":
    unittest.main()
