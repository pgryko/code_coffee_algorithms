from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:

    if len(matrix) == 0:
        return []

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    response = []
    while left < right:

        for x in range(left, right):
            response.append(matrix[top][x])
        top += 1

        for y in range(top, bottom):
            response.append(matrix[y][right - 1])

        right -= 1

        if not (left < right and top < bottom):
            break

        for x in range(right - 1, left - 1, -1):
            response.append(matrix[bottom - 1][x])

        bottom -= 1

        for y in range(bottom - 1, top - 1, -1):
            response.append(matrix[y][left])

        left += 1

    return response
