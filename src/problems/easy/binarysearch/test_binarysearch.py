import unittest

from binarysearch import search_iterative, search_recursive


class TestBinarySearchIterative(unittest.TestCase):

    def test_exists(self):
        # Test the case where target exists in array
        self.assertEqual(search_iterative([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_beginning(self):
        self.assertEqual(search_iterative([-1, 0, 3, 5, 9, 12], -1), 0)

    def test_middle(self):
        self.assertEqual(search_iterative([-1, 0, 3, 4, 5, 9, 12], 4), 3)
        self.assertEqual(search_iterative([-1, 0, 3, 5, 9, 12], 3), 2)

    def test_end(self):
        self.assertEqual(search_iterative([-1, 0, 3, 5, 9, 12], 12), 5)

    def test_not_exists(self):
        # Test the case where target exists in array
        self.assertEqual(search_iterative([-1, 0, 3, 5, 9, 12], 2), None)


class TestBinarySearchRecursive(unittest.TestCase):

    def test_exists(self):
        # Test the case where target exists in array
        self.assertEqual(search_recursive([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_beginning(self):
        self.assertEqual(search_recursive([-1, 0, 3, 5, 9, 12], -1), 0)

    def test_middle(self):
        self.assertEqual(search_recursive([-1, 0, 3, 4, 5, 9, 12], 4), 3)
        self.assertEqual(search_recursive([-1, 0, 3, 5, 9, 12], 3), 2)

    def test_end(self):
        self.assertEqual(search_recursive([-1, 0, 3, 5, 9, 12], 12), 5)

    def test_not_exists(self):
        # Test the case where target exists in array
        self.assertEqual(search_recursive([-1, 0, 3, 5, 9, 12], 2), None)
