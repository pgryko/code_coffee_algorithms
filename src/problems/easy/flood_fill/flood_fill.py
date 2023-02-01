from typing import List

"""
An image is represented by an m x n integer grid image where image[i][j] represents
the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill
on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel, plus any
pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels)
are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
"""


def is_valid(
    image: List[List[int]], row: int, col: int, prev_color: int, color: int
) -> bool:
    if row >= len(image) or row < 0:
        return False

    if col >= len(image[row]) or col < 0:
        return False

    if image[row][col] != prev_color or image[row][col] == color:
        return False

    return True


def flood_fill(image: List[List[int]], row: int, col: int, color: int):
    prev_color = image[row][col]

    # Set new color
    image[row][col] = color

    queue = [(row, col)]

    while len(queue) > 0:
        cur_row, cur_col = queue.pop()

        for per in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if is_valid(
                image,
                row=cur_row + per[0],
                col=cur_col + per[1],
                prev_color=prev_color,
                color=color,
            ):
                image[cur_row + per[0]][cur_col + per[1]] = color
                queue.append((cur_row + per[0], cur_col + per[1]))

    return image
