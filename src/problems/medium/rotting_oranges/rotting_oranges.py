# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
from typing import List
from collections import deque


def rotting_oranges(grid: List[List[int]]) -> int:

    # Similar to matrix 01, but we don't need to keep track of
    # results matrix. Instead, keep track of max time and no of unspoilt oranges

    m = len(grid)
    n = len(grid[0])
    q = deque()

    unspoilt_oranges = 0
    for i in range(0, m):
        for j in range(0, n):

            if grid[i][j] == 2:
                q.append((i, j, 0))

            elif grid[i][j] == 1:
                unspoilt_oranges = unspoilt_oranges + 1

    if unspoilt_oranges == 0:
        return 0

    direction_matrix = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    max_time = 0
    while len(q):
        x, y, time = q.popleft()

        max_time = max(time, max_time)

        for direction in direction_matrix:

            nx, ny = x + direction[0], y + direction[1]

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 2

                unspoilt_oranges = unspoilt_oranges - 1

                q.append((nx, ny, time + 1))

    return max_time if unspoilt_oranges == 0 else -1
