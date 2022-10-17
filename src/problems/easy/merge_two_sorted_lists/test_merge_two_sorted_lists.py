from merge_two_sorted_lists import ListNode


def gen_list(array: list):

    head = ListNode(array[0])
    current_head = head

    if len(array) > 1:
        for index in range(1, len(array)):
            head
