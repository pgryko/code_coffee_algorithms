import unittest

from merge_two_sorted_lists import ListNode, merge_two_lists


def gen_list(array: list) -> ListNode:
    head = ListNode(val=array[0])
    prev_node = head

    if len(array) > 1:
        for index in range(1, len(array)):
            current_node = ListNode(val=array[index])
            prev_node.next_node = current_node
            prev_node = current_node

    return head


def linkedlist_iter(list_node: ListNode):
    node = list_node

    while node:
        yield node.val
        node = node.next_node


class TestNodeFunctions(unittest.TestCase):
    def test_linked_list_iter(self):
        input_list = ["a", "b", "c", "d", "e"]

        head_node = gen_list(input_list)

        assert input_list == [x for x in linkedlist_iter(head_node)]


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_linked_list_a(self):
        # All elements in list 1 < list 2
        list_1 = gen_list([1, 2, 3])
        list_2 = gen_list([4, 5, 6])

        list_3 = merge_two_lists(list_1, list_2)

        self.assertEqual([x for x in linkedlist_iter(list_3)], [1, 2, 3, 4, 5, 6])

    def test_linked_list_b(self):
        list_1 = gen_list([1, 3, 5])
        list_2 = gen_list([2, 4, 6])

        list_3 = merge_two_lists(list_1, list_2)

        self.assertEqual([x for x in linkedlist_iter(list_3)], [1, 2, 3, 4, 5, 6])

    def test_linked_list_c(self):
        # All elements in list 1 > list 2
        list_1 = gen_list([4, 5, 6])
        list_2 = gen_list([1, 2, 3])

        list_3 = merge_two_lists(list_1, list_2)

        self.assertEqual([x for x in linkedlist_iter(list_3)], [1, 2, 3, 4, 5, 6])

    def test_linked_list_equal_first_no(self):
        list_1 = gen_list([1, 2, 4])
        list_2 = gen_list([1, 3, 4])

        list_3 = merge_two_lists(list_1, list_2)

        self.assertEqual([x for x in linkedlist_iter(list_3)], [1, 1, 2, 3, 4, 4])
