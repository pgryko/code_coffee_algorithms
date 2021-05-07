"""A simple example of a Binary search tree
"""
import copy


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.key = value
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, value=None):
        if value:
            self.root = Node(value)
            self.count = 1
        else:
            self.root = None
            self.count = 0

    def __len__(self):
        return self.count

    def search(self, value):
        pass

    def minimum(self):
        pass

    def predecessor(self, value):
        pass

    def successor(self, value):
        pass

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

    def delete(self, value):
        pass
