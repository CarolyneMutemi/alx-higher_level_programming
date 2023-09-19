#!/usr/bin/python3

"""
Has the test for the base module.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
# Base = __import__("models.base").base.Base
# Rectangle = __import__("models.rectangle").rectangle.Rectangle


class TestBase(unittest.TestCase):
    """Tests the Base class."""
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base("Hello")
        self.b4 = Base()
        self.b5 = Base(True)
        self.b6 = Base(1)
        self.b7 = Base(0)
        self.b8 = Base(-1)

    def test_id(self):
        """Tests the public instance attribute id."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, "Hello")
        self.assertEqual(self.b4.id, 2)
        self.assertEqual(self.b5.id, True)
        self.assertEqual(self.b6.id, 1)
        self.assertEqual(self.b7.id, 0)
        self.assertEqual(self.b8.id, -1)

    def test_to_json_string(self):
        """Tests the static method to_json_string."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertRaises(TypeError, Base.to_json_string, True)
        self.assertEqual(Base.to_json_string([1, 4, 5]), "[1, 4, 5]")
        self.assertEqual(Base.to_json_string({'Hello': 43}), '{"Hello": 43}')
        self.assertEqual(Base.to_json_string((2, 4, 'hello')),
                         '[2, 4, "hello"]')
        self.assertRaises(TypeError, Base.to_json_string, 23)
        self.assertEqual(Base.to_json_string('Hey'), '"Hey"')
        self.assertRaises(TypeError, Base.to_json_string, {23, 34})

    def test_save_to_file(self):
        """Tests the class method save_to_file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            str1 = '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8},'
            str2 = ' {"id": 6, "width": 2, "height": 4, "x": 0, "y": 0}]'
            check = str1 + str2
            contents = file.read()
            self.assertEqual(check, contents)

        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

        self.assertRaises(AttributeError, Rectangle.save_to_file, "Hello")
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '')
