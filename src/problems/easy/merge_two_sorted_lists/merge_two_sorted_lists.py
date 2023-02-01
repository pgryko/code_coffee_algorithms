class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    head1 = list1
    head2 = list2

    # Handle the case where we need to splice element from list 2 before list 1

    if head1.val >= head2.val:
        head_2_new = head2.next_node
        head_1_next = head1
        list1 = head2

        list1.next_node = head1
        head1_prev = list1
        head2 = head_2_new
        head1 = head_1_next

    while head1 and head2:
        if head1.val < head2.val:
            head1_prev = head1
            head1 = head1.next_node
        else:
            head2_new = head2.next_node
            head1_prev.next_node = head2
            head1_prev = head2
            head2.next_node = head1
            head2 = head2_new

    if head2:
        head1_prev.next_node = head2

    return list1
