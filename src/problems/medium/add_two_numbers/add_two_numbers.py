# Definition for singly-linked list.
from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        list_print = deque()
        list_print.append(self.val)
        next_node = self.next
        while next_node:
            list_print.append(next_node.val)
            next_node = next_node.next

        return list(list_print)

    def __str__(self):
        return str(self.to_list())


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head_listnode = None
    current_listnode = None
    current_l1 = l1
    current_l2 = l2
    remainder = 0
    while current_l1 or current_l2 or remainder:
        summ = remainder
        if current_l1:
            summ += current_l1.val
            current_l1 = current_l1.next

        if current_l2:
            summ += current_l2.val
            current_l2 = current_l2.next

        quotient = summ % 10
        remainder = summ // 10

        new_listnode = ListNode(val=quotient)

        if head_listnode is None:
            head_listnode = new_listnode
            current_listnode = new_listnode
        else:
            current_listnode.next = new_listnode
            current_listnode = new_listnode

    return head_listnode
