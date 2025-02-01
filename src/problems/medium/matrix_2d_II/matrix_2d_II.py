from typing import List

# Write an efficient algorithm that searches for a value target in an m x n integer matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# We'll use a strategy that starts from the top-right corner of the matrix.
# 2. From this position, we can make decisions based on the target value:
# - If the current value is greater than the target, we can eliminate the entire column.
# - If the current value is less than the target, we can eliminate the current row.
# - If the current value equals the target, we've found it.
# 3. We'll continue this process until we either find the target or exhaust the matrix.
# 4. This approach has a time complexity of O(m + n), where m is the number of rows
# and n is the number of columns


def search_matrix_2d_II(matrix: List[List[int]], target: int) -> bool:

    if matrix is None or len(matrix) == 0:
        return False

    if len(matrix[0]) == 0:
        return False

    # y, x
    rows, cols = len(matrix), len(matrix[0])

    row, col = 0, cols - 1

    while 0 <= row < rows and 0 <= col < cols:

        if matrix[row][col] == target:
            return True

        if matrix[row][col] > target:
            col -= 1
        if matrix[row][col] < target:
            row += 1

    return False
