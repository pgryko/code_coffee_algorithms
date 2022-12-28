import unittest

from src.problems.easy.middle_node.middle_node import middle_node, ListNode


class TestMiddleNode(unittest.TestCase):
    def test_empty_list(self):
        # create an empty linked list
        head = None
        # call the function under test
        result = middle_node(head)
        # assert that the function returns None
        self.assertIsNone(result)

    def test_single_element_list(self):
        # create a linked list with a single element
        head = ListNode(1)
        # call the function under test
        result = middle_node(head)
        # assert that the function returns the only element in the list
        self.assertEqual(result.val, 1)

    def test_even_length_list(self):
        # create a linked list with 4 elements
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        # call the function under test
        result = middle_node(head)
        # assert that the function returns the third element in the list
        self.assertEqual(result.val, 3)

    def test_odd_length_list(self):
        # create a linked list with 5 elements
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        # call the function under test
        result = middle_node(head)
        # assert that the function returns the third element in the list
        self.assertEqual(result.val, 3)
