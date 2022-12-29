import unittest

from src.problems.easy.max_height_binary_tree.max_height_binary_tree import (
    max_height_dfs,
    max_height_bfs,
    TreeNode,
)


class TestMaxHeightDFS(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_height_dfs(None), 0)

    def test_tree_with_only_root(self):
        root = TreeNode(1)
        self.assertEqual(max_height_dfs(root), 1)

    def test_tree_with_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(max_height_dfs(root), 2)

    def test_tree_with_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(max_height_dfs(root), 3)

    def test_tree_with_uneven_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(max_height_dfs(root), 3)


class TestMaxHeightBFS(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_height_bfs(None), 0)

    def test_tree_with_only_root(self):
        root = TreeNode(1)
        self.assertEqual(max_height_bfs(root), 1)

    def test_tree_with_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(max_height_bfs(root), 2)

    def test_tree_with_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(max_height_bfs(root), 3)

    def test_tree_with_uneven_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(max_height_bfs(root), 3)
