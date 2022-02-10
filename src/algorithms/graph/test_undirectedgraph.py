import unittest

from undirectedgraph import AdjacencyListGraph


class TestUndirectGraphBFS(unittest.TestCase):
    def test_simple(self):
        # Dirty but simple test by doing string cast
        graph = AdjacencyListGraph()
        graph.breath_first_search()
        self.assertEqual(
            "odict_keys([(1,BLACK, d=0), (2,BLACK, d=1), (3,BLACK, d=3), (4,BLACK, d=2), (5,BLACK, d=1)])",
            str(graph.adjacencyList.keys()),
        )
