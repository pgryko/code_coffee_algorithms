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
        mylist = LinkedList()
        self.assertEqual(len(mylist), 0)

    def test_append(self):
        mylist = LinkedList()
        mylist.append(Node(1))
        mylist.append(Node(5))
        mylist.append(Node(6))

        # Check iterating forwards from head
        self.assertEqual(mylist.head.data, 1)
        self.assertEqual(mylist.head.next.data, 5)
        self.assertEqual(mylist.head.next.next.data, 6)
        self.assertEqual(mylist.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(mylist.tail.data, 6)
        self.assertEqual(mylist.tail.prev.data, 5)
        self.assertEqual(mylist.tail.prev.prev.data, 1)
        self.assertEqual(mylist.tail.prev.prev.prev, None)

    def test_pop(self):
        mylist = LinkedList()
        mylist.append(Node(1))
        mylist.append(Node(5))
        mylist.append(Node(6))

        self.assertEqual(mylist.pop().data, 1)

        # Check iterating forwards from head
        self.assertEqual(mylist.head.data, 5)
        self.assertEqual(mylist.head.next.data, 6)
        self.assertEqual(mylist.head.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(mylist.tail.data, 6)
        self.assertEqual(mylist.tail.prev.data, 5)
        self.assertEqual(mylist.tail.prev.prev, None)

        self.assertEqual(mylist.pop().data, 5)

        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.tail.data, 6)

        self.assertEqual(mylist.head.prev, None)
        self.assertEqual(mylist.head.next, None)

        self.assertEqual(mylist.pop().data, 6)

        self.assertEqual(mylist.head, None)
        self.assertEqual(mylist.tail, None)

        self.assertRaises(IndexError, mylist.pop)

    def test_push(self):
        mylist = LinkedList()

        mylist.push(Node(1))
        mylist.push(Node(5))
        mylist.push(Node(6))

        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.tail.data, 1)

        # Check iterating forwards from head
        self.assertEqual(mylist.head.next.data, 5)
        self.assertEqual(mylist.head.next.next.data, 1)
        self.assertEqual(mylist.head.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(mylist.tail.prev.data, 5)
        self.assertEqual(mylist.tail.prev.prev.data, 6)
        self.assertEqual(mylist.tail.prev.prev.prev, None)

    def test_iterator(self):
        mylist = LinkedList()
        mylist.push(Node(1))
        mylist.push(Node(5))
        mylist.push(Node(6))

        iterator = iter(mylist)
        self.assertEqual(next(iterator).data, 6)
        self.assertEqual(next(iterator).data, 5)
        self.assertEqual(next(iterator).data, 1)
        self.assertRaises(StopIteration, iterator.__next__)


    def test_insert(self):
        mylist = LinkedList()
        mylist.insert(0, Node(1))
        mylist.insert(0, Node(5))
        mylist.insert(0, Node(6))

        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.tail.data, 1)

        # Insert node between 1 & 5
        mylist.insert(1, Node(2))
        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.tail.data, 1)

        # Check iterating forwards from head
        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.head.next.data, 2)
        self.assertEqual(mylist.head.next.next.data, 5)
        self.assertEqual(mylist.head.next.next.next.data, 1)
        self.assertEqual(mylist.head.next.next.next.next, None)

        # Check iterating backwards from tail
        self.assertEqual(mylist.tail.data, 1)
        self.assertEqual(mylist.tail.prev.data, 5)
        self.assertEqual(mylist.tail.prev.prev.data, 2)
        self.assertEqual(mylist.tail.prev.prev.prev.data, 6)
        self.assertEqual(mylist.tail.prev.prev.prev.prev, None)

if __name__ == '__main__':
    unittest.main()
