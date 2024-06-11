from __future__ import annotations

from binarysearchtrees import Node


# Is isred is set by default to true
# this allows us to call the parent class _insert while overriding its functionality
# in the child class
class RBNode(Node):
    def __init__(self, value, isred: bool = True, parent=None, left=None, right=None):
        super(RBNode, self).__init__(value, parent=parent, left=left, right=right)
        self.isRed = isred

    def __str__(self):
        return str(self.value) + (", red" if self.isRed else ", black")

    def __repr__(self):
        return (
            "Node(value="
            + str(self.value)
            + ", color="
            + ("red" if self.isRed else "black")
            + ", parent=("
            + str(self.parent)
            + "), left=("
            + str(self.left)
            + "), right=("
            + str(self.right)
            + ") )"
        )


class RedBlackTree:
    """Self-balancing binary tree where aach node has an associated colour (red or black), to ensure tree
    remains balanced during insertions and deletions.
    When tree is modified the new tree is rearranged and repainted to restore coloring properties.
    Rebalancing is not perfect but guarantees searching in O(log n) time. Insertion, deletion, search, re-arrangement
    and recoloring are also O(log n). Each node requires only one extra bit to store color information.

    Properties:
    - All nodes are either Red or Black
    - All leaf nodes are NIL
    - All NIL nodes are considered black
    - A red node does not have a red child
    - Every path from a given node to a descendant NIL goes through
    the same no. of black nodes

    Note: I'd originally wanted to inherit from the Binary tree base class, however the use of a sentinel
    means overwriting most of the methods. Hence, it was decided the simplest approach was to keep re-implement
    rather than inherit
    """

    def __init__(self, value=None):
        # For RB tree, use a sentinel as nil, instead of none. This simplifies some of the error
        # checking i.e. does node.parent exist, does node.parent.parent exist etc
        self.nil = RBNode(value=None, isred=False)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil

        # Need to check explicitly against None, as passing in value of 0
        # would cause bug
        if value is not None:
            # root node is always black
            self.root = RBNode(
                value=value, isred=False, left=self.nil, right=self.nil, parent=self.nil
            )
            self.count = 1
        else:
            self.root = self.nil
            self.count = 0

    def __len__(self):
        return self.count

    def search(self, value):
        if self.root is self.nil:
            return None

        return self._search(self.root, value)

    def _search(self, node, value):
        if node is self.nil:
            return self.nil

        if node.value == value:
            return node

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def exists(self, value):
        if self._search(self.root, value) is not self.nil:
            return True
        return False

    def minimum(self):
        if self.root is self.nil:
            return None
        return self._minimum(self.root).value

    def _minimum(self, node):
        if node.left is not self.nil:
            return self._minimum(node.left)
        else:
            return node

    def maximum(self):
        if self.root is self.nil:
            return None
        return self._maximum(self.root).value

    def _maximum(self, node):
        if node.right is not self.nil:
            return self._maximum(node.right)
        else:
            return node

    def successor(self, value):
        node = self._search(self.root, value)

        if node is self.nil:
            return None

        return self._successor(node).value

    def _successor(self, node):
        if node.right is not self.nil:
            return self._minimum(node.right)

        parent = node.parent

        while parent is not self.nil and node is parent.right:
            node = parent
            parent = node.parent

        return parent

    def __iter__(self, node: RBNode = None):
        if node is None or self.nil:
            node = self._minimum(self.root)

        while node is not self.nil:
            yield node
            node = self._successor(node)

    def _right_rotate(self, x):
        """
        For nodes, x, y, where x = y.parent, rotate the places in the tree structure
        while keeping pointer node constraints in a correct manner
        """
        # Keep track of parent node y, as we will overwrite parent.y
        y = x.left
        # Update y.left, which previously pointed to x
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, x):
        y = x.right

        x.right = y.left

        if y.left is not self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _red_black_fixup(self, node):
        # Nil is always black, hence no need to check for parent
        while node is not self.root and node.parent.isRed:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.isRed:
                    node.parent.isRed = False
                    y.isRed = False
                    node.parent.parent.isRed = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.isRed = False
                    node.parent.parent.isRed = True
                    self._right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.isRed:
                    node.parent.isRed = False
                    y.isRed = False
                    node.parent.parent.isRed = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.isRed = False
                    node.parent.parent.isRed = True
                    self._left_rotate(node.parent.parent)

        self.root.isRed = False

    def _insert(self, node, value):
        # Slightly modified version of BT insert the node
        # into the binary tree as done previously but color
        # the node red. RBNode has a default node color of red

        if value < node.value:
            if node.left is not self.nil:
                return self._insert(node.left, value)
            else:
                node.left = RBNode(
                    value, isred=True, left=self.nil, right=self.nil, parent=node
                )
                self.count += 1
                return node.left
        else:
            if node.right is not self.nil:
                return self._insert(node.right, value)
            else:
                node.right = RBNode(
                    value, isred=True, left=self.nil, right=self.nil, parent=node
                )
                self.count += 1
                return node.right

    def insert(self, value):
        """Need to overwrite root insert, so that sentinal is set
        rather than None"""

        # Handle passing in a list
        if isinstance(value, list):
            for element in value:
                self.insert(element)
            return
        # Check to see if root is empty
        if self.root is self.nil:
            self.root = RBNode(
                value, isred=False, left=self.nil, right=self.nil, parent=self.nil
            )
            self.count += 1
            return

        inserted = self._insert(self.root, value)
        self._red_black_fixup(inserted)

    def _predecessor(self, node):
        # The maximum value in the left subtree is predecessor
        if node.left is not self.nil:
            return self._maximum(node.left)

        parent = node.parent

        while parent is not self.nil and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    # Todo: replace as generator - return yield
    def predecessor(self, value):
        node = self._search(self.root, value)

        if node is self.nil:
            return None

        return self._predecessor(node).value

    def transplant(self, u: RBNode, v: RBNode):
        """RB version differs from standard BT by

        use of sentinal instead of nil and assignment of
        v.parent = u.parent, unconditionally
        """

        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_fixup(self, x: RBNode):
        # Nil is always black, hence no need to check for parent
        while x is not self.root and x.parent.isRed is False:
            if x == x.parent.left:
                w = x.parent.right
                if w.isRed:
                    w.isRed = False
                    x.parent.isRed = True
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.isRed is False and w.right.isRed is False:
                    w.isRed = True
                    x = x.parent
                else:
                    if w.right.isRed is False:
                        w.left.isRed = False
                        w.isRed = True
                        self._right_rotate(w)
                        w = x.parent.right
                    w.isRed = x.parent.isRed
                    x.parent.isRed = False
                    w.right.isRed = False
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.isRed:
                    w.isRed = False
                    x.parent.isRed = True
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.isRed is False and w.left.isRed is False:
                    w.isRed = True
                    x = x.parent
                else:
                    if w.left.isRed is False:
                        w.right.isRed = False
                        w.isRed = True
                        self._left_rotate(w)
                        w = x.parent.left
                    w.isRed = x.parent.isRed
                    x.parent.isRed = False
                    w.left.isRed = False
                    self._right_rotate(x.parent)
                    x = self.root

        x.isRed = False

    def delete(self, value):
        node = self._search(self.root, value)

        if node is None:
            return
        self._delete(node)
        return node.value

    def _delete(self, z: RBNode):
        """Similar to standard BT delete, but we maintain node y as either
        removed from the tree or moved with the tree
        """
        # Set y to equal z when  z has fewer than two children
        y = z
        y_orginal_color = y.isRed

        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            # When z has two children, set y to z's successor
            # y will move into z's position in the tree
            y = self._minimum(z.right)
            y_orginal_color = y.isRed
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.isRed

        self.count -= 1

        # If color was red, then properties hold. So
        # only change if color was black
        if y_orginal_color is False:
            self._delete_fixup(x)

    def print_tree(self):
        string_list = []
        self._print_tree(self.root, string_list)
        for line in string_list:
            print(line)  # noqa

    def _print_tree(self, node: RBNode, string_list, space: int = 0):
        string = ""
        if node is self.nil:
            return
        # handle default parameter
        if node is None:
            node = self.root
        space += 1
        self._print_tree(node.right, string_list, space)
        for i in range(1, space):
            string += "\t"
        string += str(node.value) + ("R" if node.isRed else "B")
        string_list.append(string)
        self._print_tree(node.left, string_list, space)


if __name__ == "__main__":
    from test_redblacktree import gen_balanced_tree

    tree, expected_values = gen_balanced_tree()
    tree.print_tree()
