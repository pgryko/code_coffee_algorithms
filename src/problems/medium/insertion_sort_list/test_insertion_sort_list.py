from src.problems.medium.insertion_sort_list.insertion_sort_list import (
    insertion_sort_list,
    ListNode,
)


def test_empty_list():
    # Given
    head = None

    # When
    result = insertion_sort_list(head)

    # Then
    assert result is None


def test_single_node():
    # Given
    head = ListNode(5)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == 5
    assert result.next is None


def test_two_nodes_sorted():
    # Given
    head = ListNode(1)
    head.next = ListNode(2)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next is None


def test_two_nodes_unsorted():
    # Given
    head = ListNode(2)
    head.next = ListNode(1)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next is None


def test_multiple_nodes():
    # Given
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next is None


def test_duplicate_values():
    # Given
    head = ListNode(3)
    head.next = ListNode(3)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 3
    assert result.next.next.next.next.next is None


def test_negative_numbers():
    # Given
    head = ListNode(1)
    head.next = ListNode(-3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(-1)
    head.next.next.next.next = ListNode(5)

    # When
    result = insertion_sort_list(head)

    # Then
    assert result.val == -3
    assert result.next.val == -1
    assert result.next.next.val == 1
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5
    assert result.next.next.next.next.next is None
