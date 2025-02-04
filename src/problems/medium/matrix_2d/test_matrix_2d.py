import pytest

from src.problems.medium.matrix_2d.matrix_2d import search_2d_matrix


def test_small_matrix_target_present():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 9) is True


def test_small_matrix_target_not_present():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 4) is False


def test_large_matrix_target_present():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_2d_matrix(matrix, 5) is True


def test_large_matrix_target_not_present():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_2d_matrix(matrix, 20) is False


def test_single_element_matrix_target_present():
    matrix = [[5]]
    assert search_2d_matrix(matrix, 5) is True


def test_single_element_matrix_target_not_present():
    matrix = [[5]]
    assert search_2d_matrix(matrix, 3) is False


def test_empty_matrix():
    matrix = []
    with pytest.raises(IndexError):
        search_2d_matrix(matrix, 1)


def test_target_smallest_element():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 1) is True


def test_target_largest_element():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 17) is True


def test_target_just_out_of_bounds_small():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 0) is False


def test_target_just_out_of_bounds_large():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 18) is False
