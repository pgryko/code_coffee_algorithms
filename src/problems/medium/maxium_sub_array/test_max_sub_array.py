import unittest

from src.problems.medium.maxium_sub_array.maximum_sub_array import max_sub_array


class TestTwoSums(unittest.TestCase):
    def test_a(self):
        self.assertEqual(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_b(self):
        self.assertEqual(max_sub_array([1]), 1)

    def test_c(self):
        self.assertEqual(max_sub_array([5, 4, -1, 7, 8]), 23)
