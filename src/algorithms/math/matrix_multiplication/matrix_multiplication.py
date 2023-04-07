from typing import List


def multiply(matrix_a: List[List], matrix_b: List[List]) -> List[List]:
    """Multiply two matrices using an inefficient algorithm

    Inefficient algorithm is O(n^3)

    Better performance exists with Strassen's algorithm and using numeric arrays instead of lists
    """

    matrix_a_rows = len(matrix_a)
    matrix_a_cols = len(matrix_a[0])

    matrix_b_rows = len(matrix_b)
    matrix_b_cols = len(matrix_b[0])

    # Check if the matrices can be multiplied
    assert matrix_a_cols == matrix_b_rows

    # Create a matrix to hold the result
    result = [[0 for i in range(matrix_b_cols)] for j in range(matrix_a_rows)]

    for i in range(matrix_a_rows):
        for j in range(matrix_b_cols):
            for k in range(matrix_a_cols):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result
