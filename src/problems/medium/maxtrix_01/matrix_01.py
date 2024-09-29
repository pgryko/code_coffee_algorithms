# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
from typing import List
from collections import deque


def matrix_01_nearest_zero(mat: List[List]) -> List[List]:

    m = len(mat)
    n = len(mat[0])

    # We need a matrix to store results
    result_matrix = [[-1 if mat[i][j] else 0 for j in range(0, n)] for i in range(0, m)]

    # We want to track distance from zero to -1, so append zero to que

    q = deque()
    for i in range(0, m):
        for j in range(0, n):
            if mat[i][j] == 0:
                q.append((i, j))

    while len(q):

        x, y = q.popleft()

        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for cel in neighbours:
            dx, dy = x + cel[0], y + cel[1]

            if 0 <= dx < m and 0 <= dy < n and result_matrix[dx][dy] == -1:
                result_matrix[dx][dy] = result_matrix[x][y] + 1
                q.append((dx, dy))

    return result_matrix


if __name__ == "__main__":

    print(matrix_01_nearest_zero([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
