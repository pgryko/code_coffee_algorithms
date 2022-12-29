from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_height_dfs(node: Optional[TreeNode]) -> int:
    # Recursive depth first search

    if node is None:
        return 0

    return 1 + max(max_height_dfs(node.left), max_height_dfs(node.right))


def max_height_bfs(node: Optional[TreeNode]) -> int:
    # Level Order Traversal / Breath first search
    # while adding Nodes at each level to Queue, we have to add None Node so that
    # whenever it is encountered,
    # we can increment the value of variable and that level get counted.

    queue = []
    if node:
        queue.append((node, 1))

    max_height = 0

    while len(queue) > 0:
        # Important to set index zero
        cur_node, height = queue.pop(0)

        max_height = max(max_height, height)

        if cur_node is not None:
            if cur_node.left:
                queue.append((cur_node.left, height + 1))
            if cur_node.right:
                queue.append((cur_node.right, height + 1))

    return max_height
