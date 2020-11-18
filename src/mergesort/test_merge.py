import unittest
from mergesort import merge_sort


class TestMerge(unittest.TestCase):

    def test_merge_even_A(self):
        array_in = [3, 4]
        merge_sort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [3, 4])

    def test_merge_even_B(self):
        array_in = [4, 3]
        merge_sort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [3, 4])

    def test_merge_even_B(self):
        array_in = [4, 4]
        merge_sort.merge(array_in, 0, 0, 1)
        self.assertEqual(array_in, [4, 4])

    def test_merge_odd_A(self):
        array_in = [1, 4, 2]
        merge_sort.merge(array_in, 0, 1, 2)
        self.assertEqual(array_in, [1, 2, 4])

    def test_merge_odd_A(self):
        array_in = [4, 4, 2]
        merge_sort.merge(array_in, 0, 1, 2)
        self.assertEqual(array_in, [2, 4, 4])


class TestMergeSort(unittest.TestCase):

    def test_sortbasic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 3, 4, 5, 6])

    def test_sortbasiceven(self):
        array_in = [5, 4, 2, 1, 6, 1]
        merge_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 4, 5, 6])

    def test_sortzero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in, [0, 1, 1, 2, 3, 4, 5, 6])

    def test_sortnegative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in, [-6, 1, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
