"""Example implementation of doubly linked list

"""
from typing import Union, List


class Node:
    """DataStructure Node element for a linked list"""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Node(data=" + str(self.data) + ")"


class LinkedList:
    """Double linked list, which keeps track of tail"""

    def __init__(self, nodes: List[Node] = None):
        self.nodes = []
        self.head = None
        self.tail = None
        if nodes is not None:
            # Hmm, not necessarily happy about mutating object
            node = Node(data=nodes.pop(0))
            self.head = node
            self.tail = node
            self.nodes.append(node)
            for elem in nodes:
                node.next = Node(data=elem.data)
                self.nodes.append(node.next)
                self.tail = node.next
                node = node.next

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            # When yield statement is hit, program suspends execution
            # and returns yielded value to caller
            # When a function is suspended, the state of that function is saved.
            # This includes any variable bindings local to the generator, the instruction pointer,
            # the internal stack, and any exception handling.
            # This allows you to resume function execution whenever you call one of the generator’s methods
            yield node
            node = node.next

    def reverse(self):

        prev = None
        current = self.head

        while current:
            _next = current.next
            current.next = prev
            current.prev = _next

            prev = current
            current = _next

        self.head, self.tail = self.tail, self.head

    def __str__(self):
        return str(self.nodes)

    def append(self, node: Node):
        """Insert element at end of list"""
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

        if index <= 0:
            self.push(node)
            return

        if index >= len(self.nodes):
            self.append(node)
            return

        # We will cheat and grab the ith index, as its a faster lookup
        # than iterating through the list
        ith_node = self.nodes[index]
        i_minus1_node = ith_node.prev
        self.nodes.insert(index, node)
        node.prev = ith_node.prev
        node.next = ith_node
        ith_node.prev = node
        if i_minus1_node:
            i_minus1_node.next = node
        if index == 0:
            self.head = node
        if len(self.nodes) == 1:
            self.tail = node

    def pop(self):
        """Remove and return the element at the head of the list"""

        # Technically un-needed, as attempting to pop from an
        # empty list already creates this error
        if len(self.nodes) == 0:
            raise IndexError("pop from empty list")

        elem = self.head

        new_head = elem.next
        self.head = new_head

        if new_head:
            new_head.prev = None
        else:
            self.tail = None

        # Update node's pointers to None
        elem.next = None
        elem.prev = None

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
            self.tail = prev_node
        elif next_node:
            next_node.prev = None
            self.head = next_node
        else:
            self.head = None
            self.tail = None

        # Update node's pointers to None
        cur_node.next = None
        cur_node.prev = None

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

        if not (isinstance(arg, int) or isinstance(arg, Node)):
            raise TypeError(
                "Expect arg to be of either int or Node type, received: "
                + str(type(arg))
            )

        if isinstance(arg, int):
            if arg < 0:
                raise IndexError(
                    "Arg must be a positive integer, received: " + str(int)
                )
            # Just return, if we try this on an empty list
            if len(self.nodes) == 0:
                raise IndexError("pop from empty list")
            # If index is outside list length just return
            if arg >= len(self.nodes):
                raise IndexError("Outside array index")

            return self._remove_node(arg)

        if isinstance(arg, Node):
            # Normally if we where passed a node, which had its prev/next
            # we could use that info to splice out that node.
            # However as we are built ontop of python list type,
            # we don't have access to malloc type behaviour
            # so we still need to perform a search to find the index of the node

            index = next(
                (i for i, node in enumerate(self.nodes) if node.data == arg.data), None
            )
            if index is not None:
                return self._remove_node(index)


if __name__ == "__main__":
    mylist = LinkedList()

    mylist.insert(0, Node(1))
    mylist.insert(0, Node(5))
    mylist.insert(0, Node(6))
    mylist.insert(1, Node(2))

    print(mylist)
