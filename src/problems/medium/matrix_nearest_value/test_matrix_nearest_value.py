# import unittest
# from matrix_nearest_value import breath_first_search, is_valid
#
#
# class TestMatrixNearestValue(unittest.TestCase):
#     def test_is_valid_true(self):
#         self.assertTrue(is_valid(x_len=3, y_len=3, pair=(0, 0)))
#         self.assertTrue(is_valid(x_len=3, y_len=3, pair=(0, 1)))
#         self.assertTrue(is_valid(x_len=3, y_len=3, pair=(1, 0)))
#         self.assertTrue(is_valid(x_len=3, y_len=3, pair=(1, 1)))
#         self.assertTrue(is_valid(x_len=3, y_len=3, pair=(2, 2)))
#
#     def test_is_valid_false(self):
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(-1, 0)))
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(0, -1)))
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(-1, -1)))
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(3, 2)))
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(2, 3)))
#         self.assertFalse(is_valid(x_len=3, y_len=3, pair=(3, 3)))
#
#     def test_all_zero(self):
#         self.assertEqual(
#             breath_first_search([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
#             [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#         )
#
#     def test_all_one(self):
#         self.assertEqual(
#             breath_first_search([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
#             [[9, 9, 9], [9, 9, 9], [9, 9, 9]],
#         )
#
#     def test_single(self):
#         self.assertEqual(
#             breath_first_search([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
#             [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
#         )
#
#     def test_multiple(self):
#         self.assertEqual(
#             breath_first_search([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
#             [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
#         )


import pytest
from typing import List

from src.problems.medium.matrix_nearest_value.matrix_nearest_value import (
    matrix_nearest_value,
)


# Import the matrix_nearest_value function here


@pytest.mark.parametrize(
    "input_matrix, expected_output",
    [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], [[4, 3, 2], [3, 2, 1], [2, 1, 0]]),
    ],
)
def test_matrix_nearest_value(
    input_matrix: List[List[int]], expected_output: List[List[int]]
):
    assert matrix_nearest_value(input_matrix) == expected_output


def test_empty_matrix():
    assert matrix_nearest_value([]) == []


def test_single_element_matrix():
    assert matrix_nearest_value([[0]]) == [[0]]
    assert matrix_nearest_value([[1]]) == [[-1]]


def test_large_matrix():
    large_input = [[1] * 1000 for _ in range(1000)]
    large_input[0][0] = 0
    result = matrix_nearest_value(large_input)
    assert result[0][0] == 0
    assert result[1][1] == 2
    assert result[999][999] == 1998
