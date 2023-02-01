from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    # Find the middle node of a linked list
    slow_ptr = head
    fast_ptr = head

    while fast_ptr:
        fast_ptr = fast_ptr.next

        if fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

    return slow_ptr
