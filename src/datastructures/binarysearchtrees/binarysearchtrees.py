"""A simple example of a Binary search tree
"""
from typing import Union


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Node(value=" + str(self.value) + " parent=" + str(self.parent) + \
               " left=" + str(self.left) + " right=" + str(self.right) + ")"

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

    @staticmethod
    def _minimum(node):
        """Return the minimum node

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
                return cur_node

    def minimum(self):
        """Initialises the subroutine for finding the minimum value in the tree

        """
        # Exit early if tree is empty
        if not self.root:
            return None

        return self._minimum(self.root).value

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
                return cur_node

    def maximum(self):
        """Kicks off subroutine to find maximum value"""
        # Exit early if tree is empty
        if not self.root:
            return None
        return self._maximum(self.root).value

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

    def _successor(self,node):
        """ Given a node find its successor

        Separated out into private function so that it can also be used
        in __iter__
        :param node:
        :return:
        """
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

        return parent

    def successor(self, value):
        """Find next element in sorted order
        """

        node = self._search(self.root, value)
        return self._successor(node)

    def __iter__(self, node: Node = None):

        if node is None:
            node = self._minimum(self.root)

        while node:
            yield node
            node = self._successor(node)



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

        # Handle passing in a list
        if isinstance(value, list):
            for element in value:
                self.insert(element)
            return
        # Check to see if root is empty
        if not self.root:
            self.root = Node(value)
            self.count += 1
            return

        self._insert(self.root, value)

    def _transplant(self, parent, child):
        if parent.parent is None:
            self.root = child
        elif parent == parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        if child is not None:
            child.parent = parent.parent

    def delete(self, value):

        node = self._search(self.root, value)

        if node is None:
            return None

        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            # If node has two children, then we want to replace the node, with the smallest value in the right
            # chain
            # If the right node, as no left child, it is the smallest element in the subtree

            min_child = self._minimum(node.right)
            if min_child.parent != node:
                # Min child's right value can be none
                self._transplant(min_child, min_child.right)
                min_child.right = node.right
                min_child.right.parent = min_child
            self._transplant(node, min_child)
            min_child.left = node.left
            min_child.left.parent = min_child

        self.count -= 1
        return node.value

if __name__ == '__main__':
    tree = BinarySearchTree(value=0)
    for i in range(-10, 10):
        tree.insert(i)

    iterator = iter(tree)

    while iterator:
        try:
            print(next(iterator))
        except StopIteration:
            break
