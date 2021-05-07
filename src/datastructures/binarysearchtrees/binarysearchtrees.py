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

    def _search(self, node: Node, value) -> Union[Node,None]:
        '''Recursively search binary tree

        return Node or None
        '''

        if node is None:
            return None

        if node.value == value:
            return node

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def exists(self, value):
        '''Kicks off recursive search subroutine
        '''

        if not self.root:
            return False

        if self._search(self.root, value):
            return True

        return False

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
