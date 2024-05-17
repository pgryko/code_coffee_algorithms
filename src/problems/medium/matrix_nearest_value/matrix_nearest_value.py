"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List, Tuple
from collections import deque


def is_valid(x_len: int, y_len: int, pair: Tuple):
    return 0 <= pair[0] < x_len and 0 <= pair[1] < y_len


def breath_first_search(matrix=List[List]) -> List[List]:
    x_len = len(matrix)
    y_len = len(matrix[0])

    dist = [[x_len * y_len for _ in range(0, y_len)] for _ in range(0, x_len)]

    queue = deque()

    # Loop through the matrix and find the source nodes
    # We will be searching from nodes with value zero to nodes == 1
    for x in range(0, x_len):
        for y in range(0, y_len):
            if matrix[x][y] == 0:
                dist[x][y] = 0
                queue.append((x, y))

    x_adj = [-1, 0, 1, 0]
    y_adj = [0, -1, 0, 1]

    while len(queue) > 0:
        node = queue.popleft()

        for i in range(0, 4):
            adj_node = (node[0] + x_adj[i], node[1] + y_adj[i])
            if (
                is_valid(x_len=x_len, y_len=y_len, pair=adj_node)
                and dist[node[0]][node[1]] + 1 < dist[adj_node[0]][adj_node[1]]
            ):
                dist[adj_node[0]][adj_node[1]] = dist[node[0]][node[1]] + 1
                queue.append(adj_node)

    return dist
