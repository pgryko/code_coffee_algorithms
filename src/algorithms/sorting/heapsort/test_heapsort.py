import unittest

from heapsort import build_heap, heap_sort, max_heapify


class TestMaxHeapify(unittest.TestCase):
    """
    Test the building of a maxheap from an array.
    A max heap is a loosely ordered datastructure, requiring that
    the top (root) node has a higher maximum than its leaves

    """

    def test_2_elem(self):
        array_in = [3, 4]
        max_heapify(array_in)
        self.assertEqual(array_in, [4, 3])

        array_in = [4, 3]
        max_heapify(array_in)
        self.assertEqual(array_in, [4, 3])

    def test_3_elem(self):
        array_in = [3, 5, 4]
        max_heapify(array_in)
        self.assertEqual(array_in, [5, 3, 4])

        array_in = [4, 3, 5]
        max_heapify(array_in)
        self.assertEqual(array_in, [5, 3, 4])

    def test_5_elem(self):
        array_in = [3, 5, 4, 7, 2]
        max_heapify(array_in, 1)
        self.assertEqual(array_in, [3, 7, 4, 5, 2])

        max_heapify(array_in)
        self.assertEqual(array_in, [7, 5, 4, 3, 2])

    def test_7_elem(self):
        array_in = [8, 0, 3, 3, 5, 6, 7]
        max_heapify(array_in, 1)
        self.assertEqual(array_in, [8, 5, 3, 3, 0, 6, 7])

    def test_size(self):
        """Test passing in a smaller size"""
        array_in = [3, 5, 7, 3, 0, 6, 8]
        max_heapify(array_in, 2)
        self.assertEqual(array_in, [3, 5, 8, 3, 0, 6, 7])

        array_in = [3, 5, 7, 3, 0, 6, 8, 9]
        max_heapify(array_in, 2)
        self.assertEqual(array_in, [3, 5, 8, 3, 0, 6, 7, 9])

        array_in = [3, 5, 7, 3, 0, 6, 8, 9]
        max_heapify(array_in, 2, len(array_in) - 1)
        self.assertListEqual(array_in, [3, 5, 8, 3, 0, 6, 7, 9])


class TestBuildHeap(unittest.TestCase):
    def test_build_heap(self):
        array_in = [8, 0, 3, 3, 5, 6, 7]
        build_heap(array_in)
        self.assertEqual(array_in, [8, 5, 7, 3, 0, 6, 3])


class TestMergeSort(unittest.TestCase):
    def test_sort_basic(self):
        array_in = [5, 4, 2, 1, 6, 3, 1]
        heap_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 3, 4, 5, 6])

    def test_sort_basic_even(self):
        array_in = [5, 4, 2, 1, 6, 1]
        heap_sort(array_in)
        self.assertEqual(array_in, [1, 1, 2, 4, 5, 6])

    def test_sort_zero(self):
        array_in = [5, 4, 2, 0, 1, 6, 3, 1]
        heap_sort(array_in)
        self.assertEqual(array_in, [0, 1, 1, 2, 3, 4, 5, 6])

    def test_sort_negative(self):
        array_in = [5, 4, 2, 1, -6, 3, 1]
        heap_sort(array_in)
        self.assertEqual(array_in, [-6, 1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
