#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    Tests_instantiation
    Tests_to_json_string
    Tests_save_to_file
    Tests_from_json_string
    Tests_create - line 288
    Tests_load_from_file
    Tests_save_to_file_csv
    Tests_load_from_file_csv
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase_instantiation(unittest.TestCase):
    """Unittests"""

    def test_no_argument(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_one_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_enstances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_pub(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_string(self):
        self.assertEqual("hi", Base("hi").id)

    def test_float_id(self):
        self.assertEqual(5.8, Base(5.8).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range(self):
        self.assertEqual(range(6), Base(range(6)).id)

    def test_bytes(self):
        self.assertEqual(b'Py', Base(b'Py').id)

    def test_bytearray(self):
        self.assertEqual(bytearray(b'cefg'), Base(bytearray(b'cefg')).id)

    def test_memoryview(self):
        self.assertEqual(memoryview(b'cefg'), Base(memoryview(b'cefg')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


