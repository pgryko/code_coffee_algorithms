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

    # Create dummy node to handle edge cases
    dummy = ListNode(-6000)
    dummy.next = head
    curr = head.next
    prev = head

    while curr:
        if curr.val >= prev.val:
            # If current node is greater than previous, just move forward
            prev = curr
            curr = curr.next
        else:
            # Need to find the correct position to insert curr
            temp = dummy
            # Find the position where curr should be inserted
            while temp.next.val < curr.val:
                temp = temp.next

            # Remove curr from its current position
            prev.next = curr.next

            # Insert curr in its correct position
            curr.next = temp.next
            temp.next = curr

            # Move to next node
            curr = prev.next

    return dummy.next
