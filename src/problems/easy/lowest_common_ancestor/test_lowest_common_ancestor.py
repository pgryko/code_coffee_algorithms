from src.datastructures.binarytrees.binarysearchtrees import Node

import unittest

from src.problems.easy.lowest_common_ancestor.lowest_common_ancestor import (
    lowest_common_ancestor_recursive,
    lowest_common_ancestor_iterative,
)


class TestLowestCommonAncestor(unittest.TestCase):
    def test_lowest_common_ancestor_recursive(self):
        # Create a binary search tree
        #          5
        #        /   \
        #       2     7
        #      / \   / \
        #     1   3 6   8
        #
        root = Node(5)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(8)

        # Test lowest common ancestor of nodes with values 1 and 3
        assert (
            lowest_common_ancestor_recursive(
                root, root.left.left, root.left.right
            ).value
            == 2
        )

        # Test lowest common ancestor of nodes with values 6 and 8
        assert (
            lowest_common_ancestor_recursive(
                root, root.right.left, root.right.right
            ).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 5 and 7
        assert lowest_common_ancestor_recursive(root, root.left, root.right).value == 5

        # Test lowest common ancestor of nodes with values 1 and 8
        assert (
            lowest_common_ancestor_recursive(
                root, root.left.left, root.right.right
            ).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 6 and 3
        assert (
            lowest_common_ancestor_recursive(
                root, root.right.left, root.left.right
            ).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 1 and 7
        assert (
            lowest_common_ancestor_recursive(root, root.left.left, root.right).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 2 and 3
        assert (
            lowest_common_ancestor_recursive(root, root.left, root.left.right).value
            == 2
        )

        # Test lowest common ancestor of nodes with values 6 and 7
        assert (
            lowest_common_ancestor_recursive(root, root.right.left, root.right).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 1 and 2
        assert (
            lowest_common_ancestor_recursive(root, root.left.left, root.left).value == 2
        )

        # Test lowest common ancestor of nodes with values 8 and 7
        assert (
            lowest_common_ancestor_recursive(root, root.right.right, root.right).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 6 and 5
        assert lowest_common_ancestor_recursive(root, root.right.left, root).value == 5

        # Test lowest common ancestor of nodes with values 8 and 5
        assert lowest_common_ancestor_recursive(root, root.right.right, root).value == 5

    def test_lowest_common_ancestor_iterative(self):
        # Create a binary search tree
        #          5
        #        /   \
        #       2     7
        #      / \   / \
        #     1   3 6   8
        #
        root = Node(5)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(8)

        # Test lowest common ancestor of nodes with values 1 and 3
        assert (
            lowest_common_ancestor_iterative(
                root, root.left.left, root.left.right
            ).value
            == 2
        )

        # Test lowest common ancestor of nodes with values 6 and 8
        assert (
            lowest_common_ancestor_iterative(
                root, root.right.left, root.right.right
            ).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 5 and 7
        assert lowest_common_ancestor_iterative(root, root.left, root.right).value == 5

        # Test lowest common ancestor of nodes with values 1 and 8
        assert (
            lowest_common_ancestor_iterative(
                root, root.left.left, root.right.right
            ).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 6 and 3
        assert (
            lowest_common_ancestor_iterative(
                root, root.right.left, root.left.right
            ).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 1 and 7
        assert (
            lowest_common_ancestor_iterative(root, root.left.left, root.right).value
            == 5
        )

        # Test lowest common ancestor of nodes with values 2 and 3
        assert (
            lowest_common_ancestor_iterative(root, root.left, root.left.right).value
            == 2
        )

        # Test lowest common ancestor of nodes with values 6 and 7
        assert (
            lowest_common_ancestor_iterative(root, root.right.left, root.right).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 1 and 2
        assert (
            lowest_common_ancestor_iterative(root, root.left.left, root.left).value == 2
        )

        # Test lowest common ancestor of nodes with values 8 and 7
        assert (
            lowest_common_ancestor_iterative(root, root.right.right, root.right).value
            == 7
        )

        # Test lowest common ancestor of nodes with values 6 and 5
        assert lowest_common_ancestor_iterative(root, root.right.left, root).value == 5

        # Test lowest common ancestor of nodes with values 8 and 5
        assert lowest_common_ancestor_iterative(root, root.right.right, root).value == 5
