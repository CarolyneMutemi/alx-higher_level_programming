#!/usr/bin/python3

"""
Class Square tests.
"""

import unittest
from unittest.mock import patch
import sys
from io import StringIO

sys.path.append("/home/carolyne/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
from square import Square


class TestSquare(unittest.TestCase):
    """
    Tests the class Square.
    """
    def setUp(self):
        self.s1 = Square(10)
        self.s2 = Square(2, 2)
        self.s3 = Square(10, 2, 1, 2)

    def test_size(self):
        """Tests for errors in the size attribute."""
        self.assertEqual(self.s1.size, 10)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        with self.assertRaises(ValueError):
            self.s2.size = -2
        with self.assertRaises(ValueError):
            self.s3.size = 0
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, [2])
        self.assertRaises(TypeError, Square, (1, 3))
        with self.assertRaises(TypeError):
            self.s2.size = {34}
        with self.assertRaises(TypeError):
            self.s3.size = {"size": 34}

    def test_x(self):
        """Tests for errors in the x attribute."""
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertRaises(ValueError, Square, 2, -2)
        with self.assertRaises(ValueError):
            self.s2.x = -2
        self.assertRaises(TypeError, Square, 2, "2")
        self.assertRaises(TypeError, Square, 2, [2])
        self.assertRaises(TypeError, Square, 3, (1, 3))
        with self.assertRaises(TypeError):
            self.s2.x = {34}
        with self.assertRaises(TypeError):
            self.s3.x = {"x": 34}

    def test_y(self):
        """Tests for errors in the y attribute."""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 1)
        self.assertRaises(ValueError, Square, 2, 2, -1)
        with self.assertRaises(ValueError):
            self.s2.y = -2
        self.assertRaises(TypeError, Square, 2, 1, "1", 9)
        self.assertRaises(TypeError, Square, 2, 3, [3], 0)
        self.assertRaises(TypeError, Square, 4, 3, (1, 3), 'Hello')
        with self.assertRaises(TypeError):
            self.s2.y = {34}
        with self.assertRaises(TypeError):
            self.s3.y = {"y": 34}


    def test_area(self):
        """Tests for the area method."""
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)

    def test_str(self):
        """Tests the __str__ method."""
        s1 = Square(4, 2, 1, 12)
        s2 = Square(5, 1, 0, 0)
        str1 = "[Square] (12) 2/1 - 4\n"
        str2 = "[Square] (0) 1/0 - 5\n"
        str3 = "[Square] ({}) {}/{} - {}\n"\
            .format(self.s3.id, self.s3.x, self.s3.y, self.s3.size)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(s1)
            self.assertEqual(mock_str.getvalue(), str1)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(s2)
            self.assertEqual(mock_str.getvalue(), str2)
        with patch('sys.stdout', new=StringIO()) as mock_str:
            print(self.s3)
            self.assertEqual(mock_str.getvalue(), str3)

    def test_display(self):
        """Tests the display method."""
        s1 = Square(2)
        s2 = Square(2, 2, 2)
        s3 = Square(3, 1, 0)
        display1 = "##\n##\n"
        display2 = "\n\n  ##\n  ##\n"
        display3 = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s1.display()
            self.assertEqual(mocked_display.getvalue(), display1)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s2.display()
            self.assertEqual(mocked_display.getvalue(), display2)
        with patch('sys.stdout', new=StringIO()) as mocked_display:
            s3.display()
            self.assertEqual(mocked_display.getvalue(), display3)

    def test_update(self):
        """Tests for the update method."""
        #Tests using *args.
        args = ('Hello', 1, 2, 3, 4, 3, 4, 1, 5)
        kwargs = {"id": {'id': "Me too"}, "size": 9, "x": 3, "y": 2, "Greetings": "Hello"}
        self.s1.update(89, **kwargs)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 10)
        self.s1.update(89, 2, **kwargs)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.s1.update(89, 2, 4, **kwargs)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 0)
        self.s1.update(89, 2, 4, 5, **kwargs)
        self.assertEqual(self.s1.y, 5)
        self.s2.update(*args, **kwargs)
        self.assertEqual(self.s2.id, 'Hello')
        self.assertEqual(self.s2.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 3)
        #Tests using **kwargs
        self.s3.update(**kwargs)
        self.assertEqual(self.s3.id, {'id': "Me too"})
        self.assertEqual(self.s3.size, 9)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s3.y, 2)
        with self.assertRaises(AttributeError):
            print(self.s3.Greetings)
        with self.assertRaises(KeyError):
            print(self.s3.__dict__["Greetings"])

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""
        s1 = Square(10, 2, 1)
        s2 = Square(1)
        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)
        dict1 = {'id': self.s1.id, 'size': 10, 'x': 0, 'y':0}
        dict3 = {'id': 2, 'size': 10, 'x': 2, 'y': 1}
        self.s2.update(1, 2, 3, 4)
        dict2 = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(self.s1.to_dictionary(), dict1)
        self.assertEqual(self.s3.to_dictionary(), dict3)
        self.assertEqual(self.s2.to_dictionary(), dict2)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        self.assertNotEqual(s1, s2)
