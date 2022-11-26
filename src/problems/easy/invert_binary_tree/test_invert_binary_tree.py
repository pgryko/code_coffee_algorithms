import unittest

from src.datastructures.binarytrees.test_binary_search_trees import gen_balanced_tree
from invert_binary_tree import invert


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_tree(self):
        tree, expected_values = gen_balanced_tree()

        invert(tree.root)

        iterator = iter(tree)

        self.assertEqual([x.value for x in iterator], expected_values[::-1])
