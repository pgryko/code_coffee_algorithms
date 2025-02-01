import pytest
from typing import List

from src.problems.medium.matrix_2d_II.matrix_2d_II import search_matrix_2d_II


def test_empty_matrix():
    assert search_matrix_2d_II([], 1) == False
    assert search_matrix_2d_II([[]], 1) == False


def test_single_element_matrix():
    assert search_matrix_2d_II([[1]], 1) == True
    assert search_matrix_2d_II([[1]], 2) == False


def test_small_matrix_target_present():
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert search_matrix_2d_II(matrix, 5) == True


def test_small_matrix_target_absent():
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert search_matrix_2d_II(matrix, 10) == False


def test_large_matrix_target_present():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 5) == True  # Top-left quadrant
    assert search_matrix_2d_II(matrix, 24) == True  # Bottom-right quadrant
    assert search_matrix_2d_II(matrix, 1) == True  # First element
    assert search_matrix_2d_II(matrix, 30) == True  # Last element


def test_large_matrix_target_absent():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 20) == False


def test_matrix_with_duplicates():
    matrix = [[1, 2, 2, 3], [2, 3, 3, 4], [3, 4, 4, 5]]
    assert search_matrix_2d_II(matrix, 3) == True
    assert search_matrix_2d_II(matrix, 6) == False


def test_edge_cases():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 0) == False  # Smaller than smallest
    assert search_matrix_2d_II(matrix, 31) == False  # Larger than largest
