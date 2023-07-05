#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for finding max_integer."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        a = [1, 2, 3, 4]
        self.assertEqual(max_integer(a), 4)

    def test_unordered_list(self):
        """Test list of integers."""
        b = [1, 2, 4, 3]
        self.assertEqual(max_integer(b), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        c = [4, 3, 2, 1]
        self.assertEqual(max_integer(c), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """one element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [10.53, 4.393, -3.13, 15.2, 8.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_mixed_types(self):
        "mixed types int and floats."""
        mixed_types = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed_types), 15.5)

    def test_string(self):
        """Test a string."""
        string = "chshB"
        self.assertEqual(max_integer(string), ("s"))

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
