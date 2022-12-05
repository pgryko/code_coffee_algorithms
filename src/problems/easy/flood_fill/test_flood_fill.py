import unittest

from flood_fill import is_valid, flood_fill


class TestFloodFill(unittest.TestCase):
    def test_is_valid(self):
        # Test valid case where sr and sc are within bounds and the pixel
        # at that location has the expected color
        image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(is_valid(image, 1, 1, 5, 6))

        # Test case where sr is out of bounds
        self.assertFalse(is_valid(image, 3, 1, 5, 6))
        self.assertFalse(is_valid(image, -1, 1, 5, 6))

        # Test case where sc is out of bounds
        self.assertFalse(is_valid(image, 1, 3, 5, 6))
        self.assertFalse(is_valid(image, 1, -1, 5, 6))

        # Test case where the pixel at the given location has a different
        # color than the expected value
        self.assertFalse(is_valid(image, 1, 1, 6, 7))
        # Test the case where color has not changed
        self.assertFalse(is_valid(image, 1, 1, 6, 6))

    def test_flood_fill(self):
        self.assertEqual(
            flood_fill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], row=1, col=1, color=2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        )

        self.assertEqual(
            flood_fill(image=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], row=1, col=1, color=1),
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        )
