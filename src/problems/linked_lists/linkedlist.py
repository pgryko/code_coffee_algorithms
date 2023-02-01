class Node:
    prev = None
    next = None
    val = None

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    head = None
    tail = None
    count = 0

    def __init__(self, val=None):
        if val:
            self.head = Node(val=val)
            self.tail = Node(val=val)
            self.count = 1
