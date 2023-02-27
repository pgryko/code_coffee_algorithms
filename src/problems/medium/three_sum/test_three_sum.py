import unittest

from src.problems.medium.three_sum.three_sum import three_sum


class TestTheeSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_example_2(self):
        self.assertEqual(three_sum([0, 1, 1]), [])

    def test_example_3(self):
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])

    def test_example_4(self):
        self.assertEqual(
            three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        )
