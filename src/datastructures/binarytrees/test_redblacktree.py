import unittest

from redblacktree import RedBlackTree


def gen_balanced_tree():
    """Generate a balanced tree for testing delete cases

                 0
           -5,         5
      -8      -3    3      8
    -9  -7  -4 -2  2 4  -7 -9

    """

    expected_values = [-9, -8, -7, -5, -4, -3, -2, 0, 2, 3, 4, 5, 7, 8, 9]

    tree = RedBlackTree(0)
    tree.insert([-5, 5])
    tree.insert([-8, -3, 3, 8])
    tree.insert([-9, -7, -4, -2, 2, 4, 7, 9])
    return tree, expected_values


class TestRedBlackTree(unittest.TestCase):
    def test_initialisation(self):
        self.assertEqual(len(RedBlackTree()), 0)
        self.assertEqual(len(RedBlackTree(value=5)), 1)

    def test_insert_search_unbalanced(self):
        tree = RedBlackTree()
        self.assertEqual(len(tree), 0)
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(len(tree), i + 1)

        for i in range(0, 10):
            self.assertTrue(tree.exists(i))

        tree2 = RedBlackTree(value=0)
        self.assertEqual(len(tree2), 1)
        for i in range(1, 10):
            tree2.insert(i)
            self.assertEqual(len(tree2), i + 1)

        for i in range(0, 10):
            self.assertTrue(tree2.exists(i))

        tree3 = RedBlackTree(value=0)
        self.assertEqual(len(tree3), 1)
        for i in range(-10, 10):
            tree3.insert(i)

        self.assertEqual(len(tree3), 21)

        for i in range(-10, 10):
            self.assertTrue(tree3.exists(i))

    def test_insert_search_balanced(self):
        """This also implicitly tests the list insert operation"""
        tree, expected_values = gen_balanced_tree()

        for value in expected_values:
            self.assertTrue(tree.exists(value))
        self.assertEqual(len(tree), len(expected_values))

    def test_find_minimum_maximum(self):
        tree, expected_values = gen_balanced_tree()

        self.assertEqual(tree.minimum(), -9)
        self.assertEqual(tree.maximum(), 9)

    def test_successor(self):
        tree = RedBlackTree(value=0)
        for i in range(-10, 10):
            tree.insert(i)
        for i in range(-10, 9):
            self.assertEqual(tree.successor(i), i + 1)

        # Now test inserting in a way that automatially inserts in a balanced manner
        balanced_tree, expected = gen_balanced_tree()

        for i in range(0, len(expected) - 2):
            self.assertEqual(balanced_tree.successor(expected[i]), expected[i + 1])

        self.assertIsNone(balanced_tree.successor(expected[-1]))

    def test_iterator(self):
        tree = RedBlackTree(value=0)
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
        tree = RedBlackTree(value=0)
        for i in range(-10, 10):
            tree.insert(i)

        for i in range(-9, 0):
            self.assertEqual(tree.predecessor(i), i - 1)

        for i in range(1, 10):
            self.assertEqual(tree.predecessor(i), i - 1)

    def test_delete_root(self):
        # Test inserting and deleting the root node
        tree = RedBlackTree(value=0)
        self.assertTrue(tree.exists(0))
        # Check root node is assigned
        self.assertTrue(bool(tree.root))
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.delete(0), 0)
        self.assertFalse(tree.exists(0))
        self.assertEqual(len(tree), 0)
        # Check root node is deleted
        self.assertIsNone(tree.root.value)
        self.assertFalse(tree.root.isRed)
        self.assertEqual(tree.root, tree.nil)

    def test_delete_unbalanced_tree(self):
        tree = RedBlackTree(value=0)
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

    def test_rotate(self):
        """Test right and left rotation

                Specifically map

                    9R
                8B
                    7R
            5R
                    4R
                3B
                    2R
        0B
                    -2R
                -3B
                    -4R
            -5R
                    -7R
                -8B
                    -9R

            to

                    9R
                8B
                    7R
            5R
                    4R
                3B
                    2R
        0B
                        -2R
                    -3B
                        -4R
                -5R
                    -7R
            -8B
                -9R

        """
        tree, expected_values = gen_balanced_tree()

        for value in expected_values:
            self.assertTrue(tree.exists(value))
        self.assertEqual(len(tree), len(expected_values))

        node = tree._search(node=tree.root, value=-5)
        tree._right_rotate(node)

        self.assertEqual(node.left.value, -7)
        self.assertEqual(node.right.value, -3)
        self.assertEqual(node.right.left.value, -4)
        self.assertEqual(node.right.right.value, -2)
        self.assertEqual(node.parent.value, -8)
        self.assertEqual(node.parent.left.value, -9)

        # Test walking through tree. Tree is unbalanced but constraints should still hold
        iterator = iter(tree)

        for i in range(0, len(expected_values)):
            self.assertEqual(next(iterator).value, expected_values[i])

        # Rotate back to original tree
        node = tree._search(node=tree.root, value=-8)
        tree._left_rotate(node)

        self.assertEqual(node.left.value, -9)
        self.assertEqual(node.right.value, -7)
        self.assertEqual(node.parent.value, -5)

        self.assertEqual(node.parent.right.value, -3)
        self.assertEqual(node.parent.right.left.value, -4)
        self.assertEqual(node.parent.right.right.value, -2)

        # Test walking through now balanced tree
        iterator = iter(tree)

        for i in range(0, len(expected_values)):
            self.assertEqual(next(iterator).value, expected_values[i])
