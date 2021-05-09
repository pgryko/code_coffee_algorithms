import unittest

from binarysearchtrees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_initialisation(self):
        self.assertEqual(len(BinarySearchTree()), 0)
        self.assertEqual(len(BinarySearchTree(value=5)), 1)

    def test_insert_search(self):
        tree = BinarySearchTree()
        self.assertEqual(len(tree), 0)
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(len(tree), i + 1)

        for i in range(0, 10):
            self.assertTrue(tree.exists(i))

        tree2 = BinarySearchTree(value=0)
        self.assertEqual(len(tree2), 1)
        for i in range(1, 10):
            tree2.insert(i)
            self.assertEqual(len(tree2), i + 1)

        for i in range(0, 10):
            self.assertTrue(tree2.exists(i))

        tree3 = BinarySearchTree(value=0)
        self.assertEqual(len(tree3), 1)
        for i in range(-10, 10):
            tree3.insert(i)

        self.assertEqual(len(tree3), 21)

        for i in range(-10, 10):
            self.assertTrue(tree3.exists(i))

    def test_find_minimum_maximum(self):
        self.assertIsNone(BinarySearchTree().minimum())
        self.assertIsNone(BinarySearchTree().maximum())
        tree = BinarySearchTree(value=0)
        self.assertEqual(len(tree), 1)
        for i in range(-10, 10):
            tree.insert(i)

        self.assertEqual(tree.minimum(), -10)
        self.assertEqual(tree.maximum(), 9)
