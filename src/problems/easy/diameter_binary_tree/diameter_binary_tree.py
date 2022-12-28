class Node:

    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# utility class to pass height object


class Height:
    def __init__(self):
        self.h = 0


# Optimised recursive function to find diameter
# of binary tree


def diameter_binary_tree(root: Node, height=Height()) -> int:
    # to store height of left and right subtree
    lh = Height()
    rh = Height()

    # base condition - when binary tree is empty
    if root is None:
        return 0

    # ldiameter --> diameter of left subtree
    # rdiameter  --> diameter of right subtree

    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter

    ldiameter = diameter_binary_tree(root.left, lh)
    rdiameter = diameter_binary_tree(root.right, rh)

    # height of tree will be max of left subtree
    # height and right subtree height plus1

    height.h = max(lh.h, rh.h) + 1

    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
