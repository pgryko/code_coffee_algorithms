from typing import Optional

# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
#
# The steps of the insertion sort algorithm:
#
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location
# it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially
# contains only the first element in the list. One element (red) is removed from the input data and inserted
# in-place into the sorted list with each iteration.
# Constraints:
#
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:

    if head is None or head.next is None:
        return head

    cur = head

    # create dummy node to keep track of head
    dummy = ListNode(-6000)

    while cur:

        prev = dummy

        if cur.next < cur:
            cur = cur.next
            continue

        to_insert = cur.next
        # Find the location to insert the next node
        while to_insert < prev:
            prev = prev.next

        # Then you swap

        prev.next = cur

    return dummy.next
