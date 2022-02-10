"""
Generate graphs for use in algos
"""

from collections import deque, OrderedDict


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.color = "WHITE"  # by default set color to white
        self.prev_search = None  # reference to where node was visited from
        self.distance = None  # reference to where node was visited from

    def __repr__(self):
        return (
            "(" + str(self.value) + "," + self.color + ", d=" + str(self.distance) + ")"
        )


class AdjacencyListGraph:
    def __init__(self):
        self.source_node = None
        self.adjacencyList = OrderedDict()
        self.gen_graph()

    def gen_graph(self):
        """Generate a graph

        (1) - (2)
         |  /  |   \
         (5) - (4) - (3)
        """

        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)

        self.adjacencyList[node_1] = [node_2, node_5]
        self.adjacencyList[node_2] = [node_5, node_1, node_4]
        self.adjacencyList[node_3] = [node_2, node_4]
        self.adjacencyList[node_4] = [node_2, node_5, node_3]
        self.adjacencyList[node_5] = [node_1, node_2, node_4]

        self.source_node = node_1

    def breath_first_search(self):

        # First ensure that all the nodes are colored white
        for node in self.adjacencyList.keys():
            node.color = "WHITE"
            node.distance = None
            node.prev_node = None

        source_node = self.source_node
        source_node.color = "GREY"
        source_node.distance = 0
        source_node.prev_node = None
        que = deque()
        que.appendleft(source_node)
        while len(que) > 0:
            # Pop removes from the right side of the deque
            cur_node = que.pop()
            for node in self.adjacencyList[cur_node]:
                if node.color == "WHITE":
                    node.color = "GREY"
                    node.distance = cur_node.distance + 1
                    node.prev_node = cur_node
                    que.appendleft(node)

            cur_node.color = "BLACK"


if __name__ == "__main__":
    graph = AdjacencyListGraph()
    graph.breath_first_search()
    graph.adjacencyList.keys()
