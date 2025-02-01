from typing import List

# You are given an m x n integer matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:

    # y, x
    # row, col
    m, n = len(matrix), len(matrix[0])

    left, right = 0, m * n - 1

    while left <= right:

        mid = (left + right) // 2

        row, col = mid // n, mid % n
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
