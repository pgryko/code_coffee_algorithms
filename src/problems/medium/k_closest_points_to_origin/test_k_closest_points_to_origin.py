import unittest

from src.problems.medium.k_closest_points_to_origin.k_closest_points_to_origin import (
    k_closest_points_to_origin,
)


class TestKClosestPoints(unittest.TestCase):

    def test_empty_points(self):
        self.assertEqual(k_closest_points_to_origin([], 3), [])

    def test_k_greater_than_points_length(self):
        points = [[1, 2], [2, 1], [1, 1]]
        expected_result = [[1, 1], [1, 2], [2, 1]]
        self.assertEqual(k_closest_points_to_origin(points, 5), expected_result)

    def test_k_equals_zero(self):
        points = [[1, 2], [2, 1], [1, 1]]
        self.assertEqual(k_closest_points_to_origin(points, 0), [])

    def test_normal_case(self):
        points = [[1, 2], [2, 1], [1, 1], [3, 4]]
        expected_result = [[1, 1], [1, 2], [2, 1]]
        self.assertEqual(k_closest_points_to_origin(points, 3), expected_result)

    def test_negative_coordinates(self):
        points = [[-2, -1], [-1, -1], [-3, -4], [1, 2]]
        expected_result = [[-1, -1], [-2, -1], [1, 2]]
        self.assertEqual(k_closest_points_to_origin(points, 3), expected_result)
