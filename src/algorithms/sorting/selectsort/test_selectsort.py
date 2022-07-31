import unittest

from selectsort import select_sort


class TestSelectSort(unittest.TestCase):
    def test_sortbasic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        select_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 3, 4, 5, 6])

    def test_sortzero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        select_sort(array_in)
        self.assertEqual(array_in, [0, 1, 1, 2, 3, 4, 5, 6])

    def test_sortnegative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        select_sort(array_in)
        self.assertEqual(array_in, [-6, 1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
