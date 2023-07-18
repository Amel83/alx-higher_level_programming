#!/usr/bin/python3
"""Defines unittests for square.py."""

import sys
import io
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        sq1 = Square(10)
        sq2 = Square(11)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_args(self):
        sq1 = Square(10, 4)
        sq2 = Square(4, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three_args(self):
        sq1 = Square(10, 4, 4)
        sq2 = Square(4, 4, 10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_width_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 9
        self.assertEqual(9, sq.width)

    def test_height_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 9
        self.assertEqual(9, s.height)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 9
        self.assertEqual(9, sq.size)



class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization """

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.5)
            
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong")

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)
            
    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"i": 2, "j": 4}, 2)



    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 2, 4])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2, 2, 4}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((2, 2, 4), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({2, 2, 4, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'hello')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'aabbccd'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))
            
    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'aabbccd'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"i": 2, "j": 4}, 2)
            
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "wrong")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 8.5)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [2, 2, 4])
    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({2, 2, 4, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))
            
    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {2, 2, 4})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (2, 2, 4))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({2, 2, 4, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'hello')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'aabbccd'))
    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)
            
    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'aabbccd'))



    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -10, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "wrong")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 8.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"i": 2, "j": 4})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [2, 2, 4])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {2, 2, 4})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (2, 2, 4))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({2, 2, 4, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'hello')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'aabbccd'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'aabbccdf'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -10)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square """

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong size", "]wrong x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong size", 1, "wrong y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "wrong x", "wrong y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method"""

    def test_area_small(self):
        self.assertEqual(25, Square(5, 0, 0, 1).area())

    def test_area_large(self):
        sq = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sq.area())

    def test_area_changed_attributes(self):
        sq = Square(2, 0, 0, 1)
        sq.size = 6
        self.assertEqual(36, sq.area())

    def test_area_one_arg(self):
        sq = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            sq.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ """

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        sq = Square(4)
        capture = TestSquare_stdout.capture_stdout(sq, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sq.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        sq = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(sq.id)
        self.assertEqual(correct, sq.__str__())

    def test_str_method_size_x_y(self):
        sq = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(sq.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        sq = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq))

    def test_str_method_changed_attributes(self):
        sq = Square(7, 0, 0, [4])
        sq.size = 15
        sq.x = 8
        sq.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sq))

    def test_str_method_one_arg(self):
        sq = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    def test_display_size(self):
        sq = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        sq = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        sq = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        sq = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        sq = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sq.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        sq = Square(10, 10, 10, 10)
        sq.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def test_update_args_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sq))

    def test_update_args_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def test_update_args_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sq))

    def test_update_args_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_args_more_than_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def test_update_args_width_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.width)

    def test_update_args_height_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.height)

    def test_update_args_None_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_args_None_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_args_twice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        sq.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sq))

    def test_update_args_invalid_size_type(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid")

    def test_update_args_size_zero(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, 0)

    def test_update_args_size_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, -4)

    def test_update_args_invalid_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method."""

    def test_update_kwargs_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq))

    def test_update_kwargs_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sq))

    def test_update_kwargs_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(sq))

    def test_update_kwargs_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(sq))

    def test_update_kwargs_width_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=8)
        self.assertEqual(8, sq.width)

    def test_update_kwargs_height_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=9)
        self.assertEqual(9, sq.height)

    def test_update_kwargs_None_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_kwargs_None_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_kwargs_twice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1)
        sq.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(sq))

    def test_update_kwargs_invalid_size(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)

    def test_update_kwargs_size_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-5)

    def test_update_args_and_kwargs(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def test_update_kwargs_wrong_keys(self):
        sq = Square(10, 10, 10, 10)
        sq.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def test_update_kwargs_some_wrong_keys(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(sq))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary """

    def test_to_dictionary_output(self):
        sq = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sq.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        sq1 = Square(10, 2, 1, 2)
        sq2 = Square(1, 2, 10)
        sq2.update(**s1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_arg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
