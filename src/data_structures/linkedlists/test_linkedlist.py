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

        with self.assertRaises(IndexError) as context:
            mylist.pop()

        self.assertTrue('pop from empty list', context.exception)

    def test_insert(self):
        mylist = LinkedList()
        mylist.append(Node(1))
        mylist.append(Node(5))
        mylist.append(Node(6))


if __name__ == '__main__':
    unittest.main()
