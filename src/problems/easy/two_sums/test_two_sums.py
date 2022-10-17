import unittest

from two_sum import two_sum


class TestTwoSums(unittest.TestCase):
    def test_a(self):
        self.assertEqual(two_sum(nums=[2, 7, 11, 15], target=9), [0, 1])

    def test_b(self):
        self.assertEqual(two_sum(nums=[3, 2, 4], target=6), [1, 2])

    def test_c(self):
        self.assertEqual(two_sum(nums=[3, 3], target=6), [0, 1])
