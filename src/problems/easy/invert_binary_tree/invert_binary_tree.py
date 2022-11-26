from src.datastructures.binarytrees.binarysearchtrees import Node


def invert(node: Node):

    if node is None:
        return

    invert(node.left)
    invert(node.right)

    temp_left = node.left

    node.left = node.right
    node.right = temp_left
