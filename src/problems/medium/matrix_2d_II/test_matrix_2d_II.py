from src.problems.medium.matrix_2d_II.matrix_2d_II import search_matrix_2d_II


def test_empty_matrix():
    assert search_matrix_2d_II([], 1) is False
    assert search_matrix_2d_II([[]], 1) is False


def test_single_element_matrix():
    assert search_matrix_2d_II([[1]], 1) is True
    assert search_matrix_2d_II([[1]], 2) is False


def test_small_matrix_target_present():
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert search_matrix_2d_II(matrix, 5) is True


def test_small_matrix_target_absent():
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert search_matrix_2d_II(matrix, 10) is False


def test_large_matrix_target_present():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 5) is True  # Top-left quadrant
    assert search_matrix_2d_II(matrix, 24) is True  # Bottom-right quadrant
    assert search_matrix_2d_II(matrix, 1) is True  # First element
    assert search_matrix_2d_II(matrix, 30) is True  # Last element


def test_large_matrix_target_absent():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 20) is False


def test_matrix_with_duplicates():
    matrix = [[1, 2, 2, 3], [2, 3, 3, 4], [3, 4, 4, 5]]
    assert search_matrix_2d_II(matrix, 3) is True
    assert search_matrix_2d_II(matrix, 6) is False


def test_edge_cases():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix_2d_II(matrix, 0) is False  # Smaller than smallest
    assert search_matrix_2d_II(matrix, 31) is False  # Larger than largest
