import pytest

from src.problems.medium.maxtrix_01.matrix_01 import matrix_01_nearest_zero


def test_single_zero():
    mat = [[0]]
    expected = [[0]]
    assert matrix_01_nearest_zero(mat) == expected


def test_single_one():
    mat = [[1]]
    expected = [
        [-1]
    ]  # Depending on the prompt this could be updated later to handle single element cases
    assert matrix_01_nearest_zero(mat) == expected


def test_all_zeros():
    mat = [[0, 0], [0, 0]]
    expected = [[0, 0], [0, 0]]
    assert matrix_01_nearest_zero(mat) == expected


def test_all_ones():
    mat = [[1, 1], [1, 1]]
    expected = [[-1, -1], [-1, -1]]
    assert matrix_01_nearest_zero(mat) == expected


def test_mixed_matrix():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert matrix_01_nearest_zero(mat) == expected


def test_large_matrix():
    mat = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    expected = [[0, 1, 2], [1, 2, 1], [2, 1, 0]]
    assert matrix_01_nearest_zero(mat) == expected


# Run tests
if __name__ == "__main__":
    pytest.main()
