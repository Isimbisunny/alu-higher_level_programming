#!/usr/bin/python3
"""Unit tests for the Base model."""
import unittest
import json
import os
import tempfile
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test identifiers and serialization."""

    def test_id(self):
        """Test explicit and automatic identifiers."""
        first = Base()
        self.assertEqual(Base(89).id, 89)
        self.assertEqual(Base().id, first.id + 1)

    def test_to_json(self):
        """Test JSON serialization."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(json.loads(Base.to_json_string([{"id": 1}])),
                         [{"id": 1}])

    def test_from_json(self):
        """Test JSON deserialization."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[{\"id\": 1}]"),
                         [{"id": 1}])

    def test_create(self):
        """Test instance creation from dictionaries."""
        for obj in (Rectangle(2, 3), Square(4)):
            copy = type(obj).create(**obj.to_dictionary())
            self.assertIsNot(copy, obj)
            self.assertEqual(copy.to_dictionary(), obj.to_dictionary())

    def test_files(self):
        """Test saving and loading instances."""
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                for cls, obj in ((Rectangle, Rectangle(2, 3)),
                                 (Square, Square(4))):
                    self.assertEqual(cls.load_from_file(), [])
                    cls.save_to_file([obj])
                    loaded = cls.load_from_file()
                    self.assertEqual(len(loaded), 1)
                    self.assertEqual(loaded[0].to_dictionary(),
                                     obj.to_dictionary())
                    cls.save_to_file(None)
                    self.assertEqual(cls.load_from_file(), [])
                    cls.save_to_file([])
                    self.assertEqual(cls.load_from_file(), [])
            finally:
                os.chdir(cwd)
