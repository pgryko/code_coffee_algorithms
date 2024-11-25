from src.problems.medium.insertion_sort_list.insertion_sort_list import (
    insertion_sort_list,
    ListNode,
)


def test_insertionSortList():
    # Test an empty list
    assert insertion_sort_list(None) is None

    # Test a single node list
    assert insertion_sort_list(ListNode(1)) == ListNode(1)

    # Test a list with multiple nodes in random order
    unsorted_list = ListNode(5, ListNode(2, ListNode(4, ListNode(1, ListNode(3)))))
    sorted_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert insertion_sort_list(unsorted_list) == sorted_list

    # Add more test cases to cover different scenarios and edge cases
