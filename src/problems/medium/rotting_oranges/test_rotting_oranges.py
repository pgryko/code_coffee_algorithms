import pytest

from src.problems.medium.rotting_oranges.rotting_oranges import rotting_oranges


def test_rotting_oranges():
    # Test case 1: Simple case where all fresh oranges can be rotted
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert rotting_oranges(grid) == 4

    # Test case 2: No fresh oranges, should return 0
    grid = [[2, 2, 0], [0, 2, 2], [0, 0, 2]]
    assert rotting_oranges(grid) == 0

    # Test case 3: Fresh orange disconnected from rotten oranges, return -1
    grid = [[2, 1, 0], [0, 1, 0], [0, 0, 1]]
    assert rotting_oranges(grid) == -1

    # Test case 4: All oranges are already rotten, return 0
    grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    assert rotting_oranges(grid) == 0

    # Test case 5: Mixed fresh and empty cells with no rotten oranges, return -1
    grid = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
    assert rotting_oranges(grid) == -1

    # Test case 6: No oranges at all, should return 0
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert rotting_oranges(grid) == 0


if __name__ == "__main__":
    pytest.main()
