from src.algorithms.math.matrix_multiplication import matrix_multiplication


def test_matrix_multiplication():
    matrix_a = [[1, 2, 1], [0, 1, 0], [2, 3, 4]]
    matrix_b = [[2, 5], [6, 7], [1, 8]]
    assert matrix_multiplication.multiply(matrix_a, matrix_b) == [
        [15, 27],
        [6, 7],
        [26, 63],
    ]
