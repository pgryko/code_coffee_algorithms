import unittest
from add_two_numbers import addTwoNumbers, ListNode


def gen_listnode(input_list):
    head_listnode = None
    current_listnode = None

    for number in input_list:
        if head_listnode is None:
            head_listnode = ListNode(val=number)
            current_listnode = head_listnode
        else:
            current_listnode.next = ListNode(val=number)
            current_listnode = current_listnode.next
    return head_listnode


class TestAddTwoNumber(unittest.TestCase):

    def test_simple(self):
        l1 = gen_listnode([2, 4, 3])
        l2 = gen_listnode([5, 6, 4])

        self.assertListEqual(addTwoNumbers(l1, l2).to_list(), [7, 0, 8])

    def test_zero(self):
        l1 = gen_listnode([0])
        l2 = gen_listnode([0])

        self.assertListEqual(addTwoNumbers(l1, l2).to_list(), [0])

    def test_asymetric(self):
        l1 = gen_listnode([9, 9, 9, 9, 9, 9, 9])
        l2 = gen_listnode([9, 9, 9, 9])

        self.assertListEqual(addTwoNumbers(l1, l2).to_list(), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
