from src.problems.medium.spiral_matrix.spiral_matrix import spiral_order


def test_empty_matrix():
    assert spiral_order([]) == []


def test_single_element_matrix():
    assert spiral_order([[1]]) == [1]


def test_2x2_matrix():
    matrix = [[1, 2], [3, 4]]
    assert spiral_order(matrix) == [1, 2, 4, 3]


def test_3x3_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_3x4_matrix():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
