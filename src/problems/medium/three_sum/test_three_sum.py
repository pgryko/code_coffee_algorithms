import unittest

from src.problems.medium.three_sum.three_sum import three_sum


class TestTheeSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_example_2(self):
        self.assertEqual(three_sum([0, 1, 1]), [])

    def test_example_3(self):
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
