import unittest
from src.problems.medium.clone_graph.clone_graph import Node, cloneGraph


class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        # Test case: Basic graph with multiple nodes and neighbors
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned_node1 = cloneGraph(node1)

        self.assertEqual(cloned_node1.val, node1.val)
        self.assertEqual(len(cloned_node1.neighbors), len(node1.neighbors))
        self.assertNotEqual(id(cloned_node1), id(node1))
        self.assertNotEqual(id(cloned_node1.neighbors[0]), id(node1.neighbors[0]))

    def test_clone_single_node_graph(self):
        # Test case: Single node graph
        node1 = Node(1)
        cloned_node1 = cloneGraph(node1)

        self.assertEqual(cloned_node1.val, node1.val)
        self.assertNotEqual(id(cloned_node1), id(node1))

    def test_clone_empty_graph(self):
        # Test case: Empty graph (None)
        node = None
        cloned_node = cloneGraph(node)

        self.assertEqual(cloned_node, None)

    def test_clone_circular_graph(self):
        # Test case: Circular graph
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]

        cloned_node1 = cloneGraph(node1)

        self.assertEqual(cloned_node1.val, node1.val)
        self.assertEqual(len(cloned_node1.neighbors), len(node1.neighbors))
        self.assertNotEqual(id(cloned_node1), id(node1))
        self.assertNotEqual(id(cloned_node1.neighbors[0]), id(node1.neighbors[0]))


if __name__ == "__main__":
    unittest.main()
