"""A simple example of a Binary search tree
"""
import copy
from typing import Union


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, value=None):
        # Need to check explicitly against None, as passing in value of 0
        # would cause bug
        if value is not None:
            self.root = Node(value)
            self.count = 1
        else:
            self.root = None
            self.count = 0

    def __len__(self):
        return self.count

    def _search(self, node: Node, value) -> Union[Node, None]:
        """Recursively search binary tree

        return Node or None
        """

        if node is None:
            return None

        if node.value == value:
            return node

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def exists(self, value):
        """Kicks off recursive search subroutine
        """

        if not self.root:
            return False

        if self._search(self.root, value):
            return True

        return False

    def _inorder_walk(self, node: Node):
        """Walks through the binary tree from smallest to largest

        """
        if self.node:
            self._inorder_walk(node.left)
            print(self.value)
            self._inorder_walk(node.right)

    def inorder_walk(self):
        """Kicks off inorder walk"""
        self._inorder_walk(self.root)

    @staticmethod
    def _minimum(node):
        """Return the minimum value

        This could be done recursively, but for simplicity,
        use a while loop
        """
        # Make a new reference, not strictly needed,
        # but we are updating references here
        cur_node = node

        while cur_node:
            if cur_node.left:
                cur_node = cur_node.left
            else:
                return cur_node.value

    def minimum(self):
        """Initialises the subroutine for finding the minimum value in the tree

        """
        # Exit early if tree is empty
        if not self.root:
            return None

        return self._minimum(self.root)

    @staticmethod
    def _maximum(node):
        """Return the maximum value

        This could be done recursively, but for simplicities sake,
        use a while loop
        """

        # Make a new reference, not strictly needed,
        # but we are updating references here
        cur_node = node

        while cur_node:
            if cur_node.right:
                cur_node = cur_node.right
            else:
                return cur_node.value

    def maximum(self):
        """Kicks off subroutine to find maximum value"""
        # Exit early if tree is empty
        if not self.root:
            return None
        return self._maximum(self.root)

    # Todo: replace as generator - return yield
    def predecessor(self, value):

        node = self._search(self.root, value)

        if not node:
            return None

        if node.parent:
            return node.parent.value

        elif node.left:
            return node.left.value

        return None

    # Todo: replace as generator - return yield
    def successor(self, value):
        """Find next element in sorted order"""

        node = self._search(self.root, value)

        # Handle case where value does not exist
        if not node:
            return None

        if node.right:
            return self._minimum(node.right)

        # Handle case where there is no node.right
        # We want to go up the tree and try to find the first left value

        parent = node.parent

        while parent and node == parent.right:
            node = parent
            parent = node.parent

        return parent.value

    def _insert(self, node: Node, value):
        """Given a node, transverse it until you find a node to insert into

        Update associated node links
        """

        if value < node.value:

            if node.left:
                self._insert(node.left, value)
            else:
                # Insert here and update
                node.left = Node(value)
                node.left.parent = node
                self.count += 1

        if value >= node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
                node.right.parent = node
                self.count += 1

    def insert(self, value):
        # Check to see if root is empty
        if not self.root:
            self.root = Node(value)
            self.count += 1
            return

        self._insert(self.root, value)

    # WIP
    def delete(self, value):

        node = self._search(self.root, value)

        if node is None:
            return None

        # If node has no children, simply remove it and update the parent
        if node.left is None and node.right is None:

            if node.parent.right == node:
                node.parent.right = None
            else:
                node.parent.left = None

            node.parent = None
            self.count = self.count - 1
            return node.value

        # If node has only one child
        if bool(node.left) != bool(node.right):
            # Check to see if its left node that exists
            if node.left:
                # Set the replacement node to point to
                # the correct grand-parent (now parent)
                node.left.parent = node.parent
                # Update the grand-parent's reference
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            # Otherwise right node exists
            else:
                node.right.parent = node.right
                # Update the grand-parent's reference
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right


if __name__ == '__main__':
    tree = BinarySearchTree(value=0)
    for i in range(-10, 10):
        tree.insert(i)

    tree.inorder_walk()
