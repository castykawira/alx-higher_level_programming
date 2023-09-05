#!/usr/bin/python3
"""Unit tests for the max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test when the input list is ordered in ascending order"""
        result = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(result), 5)

    def test_unordered_list(self):
        """Test when the input list is unordered"""
        result = [3, 1, 4, 5, 2]
        self.assertEqual(max_integer(result), 5)

    def test_max_at_begginning(self):
        """Test when the maximum value is at the beginning of the input list"""
        result = [5, 2, 3, 4, 1]
        self.assertEqual(max_integer(result), 5)

    def test_empty_list(self):
        """Test when the input list is empty"""
        result = []
        self.assertEqual(max_integer(result), None)

    def test_one_element_list(self):
        """Test when the input list contains only one element"""
        result = [5]
        self.assertEqual(max_integer(result), 5)

    def test_floats(self):
        """Test when the input list contains floating-point numbers"""
        result = [3.5, 7.2, 2.1, 9.7, 1.0]
        self.assertEqual(max_integer(result), 9.7)

    def test_ints_and_floats(self):
        """Test when the list contains integers and floating-point numbers"""
        result = [3, 7.2, 2, 9.7, 1]
        self.assertEqual(max_integer(result), 9.7)

    def test_string(self):
        """Test when the input list contains string values"""
        result = "Deborah"
        self.assertEqual(max_integer(result), 'r')

    def test_list_of_strings(self):
        """Test when the input list contains strings"""
        result = ["apple", "banana", "cherry", "date"]
        self.assertEqual(max_integer(result), "date")

    def test_empty_string(self):
        """Test when the input list contains empty strings"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
