"""Example implementation of doubly linked list

"""

from typing import Union


class Node:
    """DataStructure Node element for a linked list
    """

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Double linked list, which keeps track of tail
    """

    def __init__(self, node: Node = None):
        self.nodes = []
        self.head = None
        self.tail = None
        if node is not None:
            self.nodes.append(node)
            self.head = node
            self.tail = node

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        return str(self.nodes)

    def append(self, node: Node):
        """Insert element at end of list
        """
        self.nodes.append(node)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def push(self, node: Node):
        """Insert element at head of list"""
        self.nodes.insert(0, node)

        if self.head:
            self.head.prev = node
            node.next = self.head

        self.head = node
        node.prev = None

        if self.tail is None:
            self.tail = node

    def insert(self, index: int, node: Node):
        """Insert element at specific index.
        If index is greater than list size, or
        if list is empty
        then append to the end.
        """
        if index >= len(self.nodes):
            self.append(node)
            return

        # We will cheat and grab the ith index, as its a faster lookup
        # than iterating through the list
        ith_node = self.nodes[index]
        node.prev = ith_node.prev
        node.next = ith_node
        self.nodes.insert(index, node)
        ith_node.prev = node

    def pop(self):
        """Remove and return the element at the head of the list
        """

        # Technically un-needed, as attempting to pop from an
        # empty list already creates this error
        if len(self.nodes) == 0:
            raise IndexError('pop from empty list')

        elem = self.head

        new_head = elem.next
        self.head = new_head

        if new_head:
            new_head.prev = None
        else:
            self.tail = None

        return self.nodes.pop(0)

    def _remove_node(self, index: int) -> Union[Node, None]:
        """Private member function to handle correct pointer updates,
        when removing a node
        """
        cur_node = self.nodes.pop(index)

        prev_node = cur_node.prev
        next_node = cur_node.next

        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif prev_node:
            prev_node.next = None
        else:
            next_node.prev = None

        return cur_node

    def remove(self, arg: Union[int, Node]) -> Union[Node, None]:
        """Remove either an element from a list, and return it.

        Can either pass in:
        * An index describing the location of the Node,
        * A node instance with a NOT None value in prev or next
        * A node with a value, but both prev & next are None (performs a linear search)

        :param arg: int (index of element to remove), Node element to search for and remove
        :return: Node or None
        """

        if not isinstance(arg, int) or not isinstance(arg, Node):
            raise ValueError("Expect arg to be of either int or Node type, received: "
                             + str(type(arg)))

        if isinstance(arg, int):
            if arg < 0:
                raise ValueError("Arg must be a positive integer, received: " + str(int))
            # Just return, if we try this on an empty list
            if len(self.nodes) == 0:
                raise IndexError('pop from empty list')
            # If index is outside list length just return
            if arg >= len(self.nodes):
                raise IndexError('Outside array index')

            return self._remove_node(arg)

        if isinstance(arg, Node):
            # Normally if we where passed a node, which had its prev/next
            # we could use that info to splice out that node.
            # However as we are built ontop of python list type,
            # we don't have access to malloc type behaviour
            # so we still need to perform a search to find the index of the node

            index = next((i for i, node in enumerate(self.nodes) if node.data == arg.data), None)

            if index:
                return self._remove_node(arg)


if __name__ == '__main__':
    mylist = LinkedList()

    mylist.append(Node(1))
    mylist.append(Node(5))
    mylist.append(Node(6))

    print(mylist)

    mylist.insert(1, Node(17))

    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
