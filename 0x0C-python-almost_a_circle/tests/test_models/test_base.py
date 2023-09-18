#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    Test cases for the base class
'''


class test_base(unittest.TestCase):
    '''
        Testing cases for the Base class
    '''
    def test_id_none(self):
        '''
            Test creating a Base instance with id set to None
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Test creating a Base instance with a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Test creating a Base instance with id set to 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Test creating a Base instance with a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            Test creating a Base instance with a string id
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
            Test creating a Base instance with a list id
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
            Test creating a Base instance with a dictionary id
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
            Test creating a Base instance with a tuple id
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        '''
            Test the type of the returned JSON string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Test the value of the returned JSON string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        '''
            Test to_json_string with None as input
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Test to_json_string with an empty list as input
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level resources for the test suite
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Test if the module has a docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test if the Square class has a docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Test if methods of the Square class have docstrings
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
