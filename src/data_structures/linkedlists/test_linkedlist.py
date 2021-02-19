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

    def test_pop(self):
        mylist = LinkedList()
        mylist.append(Node(1))
        mylist.append(Node(5))
        mylist.append(Node(6))

        self.assertEqual(mylist.pop().data, 1)
        self.assertEqual(mylist.pop().data, 5)
        self.assertEqual(mylist.pop().data, 6)

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

        # Todo, add iterator and next

    def test_insert(self):
        mylist = LinkedList()
        mylist.insert(0, Node(1))
        mylist.insert(0, Node(5))
        mylist.insert(0, Node(6))

        self.assertEqual(mylist.head.data, 6)
        self.assertEqual(mylist.tail.data, 1)

        # Todo test updating of head/tail and pointers


if __name__ == '__main__':
    unittest.main()
