from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    node_map: Dict[Node, Node] = {}

    def clone(node: Node, node_map: Dict[Node, Node]) -> Node | None:
        if node is None:
            return

        if node in node_map:
            return node_map[node]

        node_map[node] = Node(val=node.val)

        for ajd_node in node.neighbors:
            node_map[node].neighbors.append(clone(node=ajd_node, node_map=node_map))

        return node_map[node]

    return clone(node, node_map)
