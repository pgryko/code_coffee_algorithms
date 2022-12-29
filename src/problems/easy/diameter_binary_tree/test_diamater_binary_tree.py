import unittest

from src.problems.easy.diameter_binary_tree.diameter_binary_tree import (
    diameter_binary_tree,
    Node,
)


class TestDiameterOpt(unittest.TestCase):
    def test_empty_tree(self):
        # create an empty tree
        root = None
        # call the function under test
        result = diameter_binary_tree(root)
        # assert that the function returns 0 and the height is 0
        self.assertEqual(result, 0)

    def test_tree_with_left_child(self):
        # create a tree with a single left child
        root = Node(1)
        root.left = Node(2)
        # call the function under test
        result = diameter_binary_tree(root)
        # assert that the function returns 2 (the diameter of the tree) and the height is 2
        self.assertEqual(result, 2)

    def test_tree_with_right_child(self):
        # create a tree with a single right child
        root = Node(1)
        root.right = Node(2)
        # call the function under test
        result = diameter_binary_tree(root)
        # assert that the function returns 2 (the diameter of the tree) and the height is 2
        self.assertEqual(result, 2)

    def test_tree_with_left_and_right_children(self):
        # create a tree with a left and right child
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        # call the function under test
        result = diameter_binary_tree(root)
        # assert that the function returns 3 (the diameter of the tree)
        self.assertEqual(result, 3)
