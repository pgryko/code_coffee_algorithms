import unittest
from mergesort import MergeSort


class TestMerge(unittest.TestCase):
    def test_merge_even_a(self):
        array_in = [3, 4]
        MergeSort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [3, 4])

    def test_merge_even_b(self):
        array_in = [4, 3]
        MergeSort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [3, 4])

    def test_merge_even_c(self):
        array_in = [4, 4]
        MergeSort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [4, 4])

    def test_merge_odd_a(self):
        array_in = [1, 4, 2]
        MergeSort.merge(array_in, 0, 1, 2)
        self.assertEqual(array_in, [1, 2, 4])


class TestMergesort(unittest.TestCase):
    def test_sort_basic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        MergeSort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 3, 4, 5, 6])

    def test_sort_basic_even(self):
        array_in = [5, 4, 2, 1, 6, 1]
        MergeSort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 4, 5, 6])

    def test_sort_zero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        MergeSort(array_in)
        self.assertEqual(array_in, [0, 1, 1, 2, 3, 4, 5, 6])

    def test_sort_negative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        MergeSort(array_in)
        self.assertEqual(array_in, [-6, 1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
