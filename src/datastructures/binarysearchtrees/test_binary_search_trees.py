import unittest

from binarysearchtrees import BinarySearchTree


def gen_balanced_tree():
    """Generate a balanced tree for testing delete cases

                 0
           -5,         5
      -8      -3    3      8
    -9  -7  -4 -2  2 4  -7 -9

    """

    expected_values = [-9, -8, -7, -5, -4, -3, -2, 0, 2, 3, 4, 5, 7, 8, 9]

    tree = BinarySearchTree(0)
    tree.insert([-5, 5])
    tree.insert([-8, -3, 3, 8])
    tree.insert([-9, -7, -4, -2, 2, 4, 7, 9])
    return tree, expected_values


class TestBinarySearchTree(unittest.TestCase):

    def test_initialisation(self):
        self.assertEqual(len(BinarySearchTree()), 0)
        self.assertEqual(len(BinarySearchTree(value=5)), 1)

    def test_insert_search_unbalanced(self):
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

    def test_insert_search_balanced(self):
        '''This also implicitly tests the list insert operation'''
        tree, expected_values = gen_balanced_tree()

        for value in expected_values:
            self.assertTrue(tree.exists(value))
        self.assertEqual(len(tree), len(expected_values))

    def test_find_minimum_maximum(self):
        tree, expected_values = gen_balanced_tree()

        self.assertEqual(tree.minimum(), -9)
        self.assertEqual(tree.maximum(), 9)

    def test_successor(self):
        tree = BinarySearchTree(value=0)
        for i in range(-10, 10):
            tree.insert(i)
        for i in range(-10, 0):
            self.assertEqual(tree.successor(i).value, i + 1)

        # We are not enforcing a uniqueness constraint, so there are two entries for
        # zero
        self.assertEqual(tree.successor(0).value, 0)

        for i in range(1, 9):
            self.assertEqual(tree.successor(i).value, i + 1)

        # Now test a balanced tree
        balanced_tree, expected = gen_balanced_tree()

        for i in range(0, len(expected) - 2):
            self.assertEqual(balanced_tree.successor(
                expected[i]).value, expected[i + 1])

        self.assertIsNone(balanced_tree.successor(expected[-1]))

    def test_iterator(self):
        tree = BinarySearchTree(value=0)
        for i in range(-10, 10):
            tree.insert(i)

        iterator = iter(tree)
        for i in range(-10, 0):
            self.assertEqual(next(iterator).value, i)

        # We are not enforcing a uniqueness constraint, so there are two entries for
        # zero
        self.assertEqual(next(iterator).value, 0)

        for i in range(0, 9):
            self.assertEqual(next(iterator).value, i)

        # Now test a balanced tree
        balanced_tree, expected = gen_balanced_tree()

        iterator = iter(balanced_tree)

        for i in range(0, len(expected)):
            self.assertEqual(next(iterator).value, expected[i])

        self.assertRaises(StopIteration, iterator.__next__)

    def test_predecessor(self):
        tree = BinarySearchTree(value=0)
        for i in range(-10, 10):
            tree.insert(i)

        for i in range(-9, 0):
            self.assertEqual(tree.predecessor(i), i - 1)

        for i in range(1, 10):
            self.assertEqual(tree.predecessor(i), i - 1)

    def test_delete_root(self):
        # Test inserting and deleting the root node
        tree = BinarySearchTree(value=0)
        self.assertTrue(tree.exists(0))
        # Check root node is assigned
        self.assertTrue(bool(tree.root))
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.delete(0), 0)
        self.assertFalse(tree.exists(0))
        self.assertEqual(len(tree), 0)
        # Check root node is deleted
        self.assertIsNone(tree.root)

    def test_delete_unbalanced_tree(self):
        tree = BinarySearchTree(value=0)
        self.assertEqual(len(tree), 1)
        for i in range(-10, 10):
            tree.insert(i)

        self.assertEqual(len(tree), 21)

        for i in range(-10, 10):
            self.assertTrue(tree.exists(i))

        for i in range(-10, 0):
            self.assertEqual(tree.delete(i), i)
            self.assertFalse(tree.exists(i))
            self.assertEqual(len(tree), 10 - i)

        # There are two instances of zero (we initialize with value=0
        # and push and additional zero with range function
        tree.delete(0)
        self.assertTrue(tree.exists(0))

        for i in range(0, 10):
            self.assertEqual(tree.delete(i), i)
            self.assertFalse(tree.exists(i))
            self.assertEqual(len(tree), 9 - i)

        self.assertEqual(len(tree), 0)

    def test_delete_balanced_tree(self):
        # Test a more general case of deleting a node in a binary tree
        tree, expected_values = gen_balanced_tree()
        self.assertEqual(len(tree), len(expected_values))

        for i in expected_values:
            self.assertTrue(tree.exists(i))

        for i in expected_values:
            self.assertEqual(tree.delete(i), i)
            self.assertFalse(tree.exists(i))

        self.assertEqual(len(tree), 0)
