import unittest

from linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):
    '''
    Test initialisation of node class
    '''

    def test_initialisation(self):
        new_node = Node(data="Arbitrary string")

        self.assertEqual(new_node.data, "Arbitrary string")


class TestLinkedList(unittest.TestCase):
    '''Test behaviour of linked list
    '''

    def test_initialisation(self):
        my_list = LinkedList()
        self.assertEqual(len(my_list), 0)

    def test_append(self):
        my_list = LinkedList()
        my_list.append(Node(1))
        my_list.append(Node(5))
        my_list.append(Node(6))

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 1)
        self.assertEqual(my_list.head.next.data, 5)
        self.assertEqual(my_list.head.next.next.data, 6)
        self.assertEqual(my_list.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 6)
        self.assertEqual(my_list.tail.prev.data, 5)
        self.assertEqual(my_list.tail.prev.prev.data, 1)
        self.assertEqual(my_list.tail.prev.prev.prev, None)

    def test_pop(self):
        my_list = LinkedList()
        my_list.append(Node(1))
        my_list.append(Node(5))
        my_list.append(Node(6))

        self.assertEqual(my_list.pop().data, 1)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 5)
        self.assertEqual(my_list.head.next.data, 6)
        self.assertEqual(my_list.head.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 6)
        self.assertEqual(my_list.tail.prev.data, 5)
        self.assertEqual(my_list.tail.prev.prev, None)

        self.assertEqual(my_list.pop().data, 5)

        self.assertEqual(my_list.head.data, 6)
        self.assertEqual(my_list.tail.data, 6)

        self.assertEqual(my_list.head.prev, None)
        self.assertEqual(my_list.head.next, None)

        self.assertEqual(my_list.pop().data, 6)

        self.assertEqual(my_list.head, None)
        self.assertEqual(my_list.tail, None)

        self.assertRaises(IndexError, my_list.pop)

    def test_push(self):
        my_list = LinkedList()

        my_list.push(Node(1))
        my_list.push(Node(5))
        my_list.push(Node(6))

        self.assertEqual(my_list.head.data, 6)
        self.assertEqual(my_list.tail.data, 1)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.next.data, 5)
        self.assertEqual(my_list.head.next.next.data, 1)
        self.assertEqual(my_list.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.prev.data, 5)
        self.assertEqual(my_list.tail.prev.prev.data, 6)
        self.assertEqual(my_list.tail.prev.prev.prev, None)

    def test_iterator(self):
        my_list = LinkedList()
        my_list.push(Node(1))
        my_list.push(Node(5))
        my_list.push(Node(6))

        iterator = iter(my_list)
        self.assertEqual(next(iterator).data, 6)
        self.assertEqual(next(iterator).data, 5)
        self.assertEqual(next(iterator).data, 1)
        self.assertRaises(StopIteration, iterator.__next__)

    def test_insert(self):
        my_list = LinkedList()
        my_list.insert(0, Node(1))
        my_list.insert(0, Node(5))
        my_list.insert(0, Node(6))

        self.assertEqual(my_list.head.data, 6)
        self.assertEqual(my_list.tail.data, 1)

        # Insert node between 1 & 5
        my_list.insert(1, Node(2))
        self.assertEqual(my_list.head.data, 6)
        self.assertEqual(my_list.tail.data, 1)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 6)
        self.assertEqual(my_list.head.next.data, 2)
        self.assertEqual(my_list.head.next.next.data, 5)
        self.assertEqual(my_list.head.next.next.next.data, 1)
        self.assertEqual(my_list.head.next.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 1)
        self.assertEqual(my_list.tail.prev.data, 5)
        self.assertEqual(my_list.tail.prev.prev.data, 2)
        self.assertEqual(my_list.tail.prev.prev.prev.data, 6)
        self.assertEqual(my_list.tail.prev.prev.prev.prev, None)

    def test_remove_node(self):
        """Test removal of a specific node"""

        my_list = LinkedList()

        with self.assertRaises(IndexError):
            my_list.remove(0)

        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)

        my_list.append(node_1)
        my_list.append(node_2)
        my_list.append(node_3)
        my_list.append(node_4)
        my_list.append(node_5)

        with self.assertRaises(TypeError):
            my_list.remove('a')

        with self.assertRaises(IndexError):
            my_list.remove(-1)

        removed_node = my_list.remove(Node(2))

        self.assertEqual(node_2, removed_node)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 1)
        self.assertEqual(my_list.head.next.data, 3)
        self.assertEqual(my_list.head.next.next.data, 4)
        self.assertEqual(my_list.head.next.next.next.data, 5)
        self.assertEqual(my_list.head.next.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 5)
        self.assertEqual(my_list.tail.prev.data, 4)
        self.assertEqual(my_list.tail.prev.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev.prev.data, 1)
        self.assertEqual(my_list.tail.prev.prev.prev.prev, None)

        my_list.remove(node_1)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 3)
        self.assertEqual(my_list.head.next.data, 4)
        self.assertEqual(my_list.head.next.next.data, 5)
        self.assertEqual(my_list.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 5)
        self.assertEqual(my_list.tail.prev.data, 4)
        self.assertEqual(my_list.tail.prev.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev.prev, None)

        my_list.remove(node_5)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 3)
        self.assertEqual(my_list.head.next.data, 4)
        self.assertEqual(my_list.head.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 4)
        self.assertEqual(my_list.tail.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev, None)

    def test_remove_index(self):
        my_list = LinkedList()

        with self.assertRaises(IndexError):
            my_list.remove(0)

        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)

        my_list.append(node_1)
        my_list.append(node_2)
        my_list.append(node_3)
        my_list.append(node_4)
        my_list.append(node_5)

        removed_node = my_list.remove(1)

        self.assertEqual(node_2, removed_node)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 1)
        self.assertEqual(my_list.head.next.data, 3)
        self.assertEqual(my_list.head.next.next.data, 4)
        self.assertEqual(my_list.head.next.next.next.data, 5)
        self.assertEqual(my_list.head.next.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 5)
        self.assertEqual(my_list.tail.prev.data, 4)
        self.assertEqual(my_list.tail.prev.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev.prev.data, 1)
        self.assertEqual(my_list.tail.prev.prev.prev.prev, None)

        my_list.remove(0)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 3)
        self.assertEqual(my_list.head.next.data, 4)
        self.assertEqual(my_list.head.next.next.data, 5)
        self.assertEqual(my_list.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 5)
        self.assertEqual(my_list.tail.prev.data, 4)
        self.assertEqual(my_list.tail.prev.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev.prev, None)

        my_list.remove(2)

        # Check iterating forwards from head
        self.assertEqual(my_list.head.data, 3)
        self.assertEqual(my_list.head.next.data, 4)
        self.assertEqual(my_list.head.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(my_list.tail.data, 4)
        self.assertEqual(my_list.tail.prev.data, 3)
        self.assertEqual(my_list.tail.prev.prev, None)

    def test_reverse(self):
        my_list = LinkedList(nodes=[Node('A'), Node('B'), Node('C'), Node('D')])

        my_list.reverse()


if __name__ == '__main__':
    unittest.main()
