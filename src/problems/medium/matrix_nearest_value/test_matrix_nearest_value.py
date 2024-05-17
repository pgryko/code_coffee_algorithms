import unittest
from matrix_nearest_value import breath_first_search, is_valid


class TestMatrixNearestValue(unittest.TestCase):
    def test_is_valid_true(self):
        self.assertTrue(is_valid(x_len=3, y_len=3, pair=(0, 0)))
        self.assertTrue(is_valid(x_len=3, y_len=3, pair=(0, 1)))
        self.assertTrue(is_valid(x_len=3, y_len=3, pair=(1, 0)))
        self.assertTrue(is_valid(x_len=3, y_len=3, pair=(1, 1)))
        self.assertTrue(is_valid(x_len=3, y_len=3, pair=(2, 2)))

    def test_is_valid_false(self):
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(-1, 0)))
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(0, -1)))
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(-1, -1)))
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(3, 2)))
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(2, 3)))
        self.assertFalse(is_valid(x_len=3, y_len=3, pair=(3, 3)))

    def test_all_zero(self):
        self.assertEqual(
            breath_first_search([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )

    def test_all_one(self):
        self.assertEqual(
            breath_first_search([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            [[9, 9, 9], [9, 9, 9], [9, 9, 9]],
        )

    def test_single(self):
        self.assertEqual(
            breath_first_search([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        )

    def test_multiple(self):
        self.assertEqual(
            breath_first_search([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
        )
