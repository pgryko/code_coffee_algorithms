import unittest
from mergesort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_sortbasic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 3, 4, 5, 6])

    def test_sortzero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in,[0, 1, 1, 2, 3, 4, 5, 6])

    def test_sortnegative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        merge_sort(array_in)
        self.assertEqual(array_in,[-6, 1, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()