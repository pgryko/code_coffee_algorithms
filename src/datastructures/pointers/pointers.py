"""Example of implementing linked list with pointers in an array

Usage: $ python3 pointers.py

"""


# https://omkarpathak.in/2018/04/11/python-getitem-and-setitem/
class LinkedListSingleArray:
    """A doubly linked list implemented using a single array, with a custom pointer implementation

    A stack is used as a free list to keep track of free space in allocated buffer.
    Buffer is doubled in size of element is pushed beyond container capacity
    """

    def __init__(self, data: list = None, capacity: int = 20):

        # Make sure capacity is greater than 1, otherwise
        # resize function will fail
        if capacity < 1:
            capacity = 2

        # If initial data is supplied, make sure that capacity is greater than origianl list size
        if data:
            capacity = max(capacity, len(data))
        # Create an empty buffer (malloc), and populate 'pointer' to free elements
        # Buffer array is partitioned into blocks of 3, with |prev, key, next|
        # e.g.
        # [|prev,key,next|, |prev, key, next|, |prev, key, next| ]
        # where the 'pointers', point to the next/prev key
        # e.g for an empty array [None, 0, 4, None, 0, 7, None, 0, None]
        self._buffer = [
            x + 2 if ((x + 1) % 3 == 0) else 0 if ((x + 2) % 3 == 0) else None
            for x in range(0, capacity * 3)
        ]
        # Set end element to None
        self._buffer[-1] = None
        self._free_index = 1
        self._count = 0
        self._head = None
        self._tail = None

        if data:
            for elem in data:
                self.push(elem)

    def __next__(self, index=None):

        if index:
            if (index + 2) % 3 != 0:
                raise IndexError("Index does not appear to be valid")
            current_index = index
        else:
            current_index = self._head

        while current_index:
            data = self._buffer[current_index]
            yield data
            current_index = self._buffer[current_index + 1]

    def __prev__(self, index=None):
        """Function to iterate backwards.

        Not a standard python magic function, but implemented here,
        as this is a doubly liked list

        """

        if index:
            if (index + 2) % 3 != 0:
                raise IndexError("Index does not appear to be valid")
            current_index = index
        else:
            # By default set current to tail, so we can iterate backwards
            current_index = self._tail

        while current_index:
            data = self._buffer[current_index]
            yield data
            current_index = self._buffer[current_index - 1]

    def _get_next_index(self, current_index):
        """Helper function to get index of next element"""

        if (current_index + 2) % 3 != 0:
            raise IndexError("Index does not appear to be valid")

        return self._buffer[current_index + 1]

    def _get_prev_index(self, current_index):
        """Helper function to get index of prev element"""

        if (current_index + 2) % 3 != 0:
            raise IndexError("Index does not appear to be valid")

        return self._buffer[current_index - 1]

    def reverse(self):
        """Reverses the linked list in place"""

        prev = None
        curr = self._head

        while curr:
            _next = self._get_next_index(curr)

            self._buffer[curr + 1] = prev
            self._buffer[curr - 1] = _next

            prev = curr
            curr = _next

        self._head, self._tail = self._tail, self._head

    def __len__(self):
        return self._count

    def capacity(self):
        return len(self._buffer) // 3

    def _resize(self):
        """Increase the size of the array buffer and
        update free list. Different implementations have a different scalar factors,
        either 2x or 1.5 based on assumptions made in amortized analysis.
        Here we just double the size of the buffer
        """
        init_size = len(self._buffer)

        self._buffer.extend(
            [
                x + 2 if ((x + 1) % 3 == 0) else 0 if ((x + 2) % 3 == 0) else None
                for x in range(init_size, init_size * 2)
            ]
        )
        self._buffer[-1] = None
        # Two cases, either there is no more free space, so we just update the free index
        if self._free_index is None:
            self._free_index = init_size + 1
        else:
            # we need to iterate through the free array stack and update it's next
            current_free = self._free_index
            while self._buffer[current_free + 1] is not None:
                current_free = self._buffer[current_free + 1]

            self._buffer[current_free + 1] = init_size + 1

    def push(self, element):
        """Insert an element into the list"""

        if self._free_index is None:
            self._resize()

        insert_index = self._free_index

        next_free = self._get_next_index(self._free_index)
        # Insert element into location of current free element

        self._buffer[insert_index] = element
        self._count += 1
        # As element is set to head of list, set prev to None
        self._buffer[insert_index - 1] = None
        # Update free list
        self._free_index = next_free

        if self._head is None:
            self._head = insert_index
            # Set next to None
            self._buffer[insert_index + 1] = None
            # If done correctly prev, should already be None
            self._buffer[insert_index - 1] = None
            # Update tail to also point to current element (at this point
            # we have only one element)
            self._tail = insert_index

        else:
            # Updated prev, on old head to point to new head
            self._buffer[self._head - 1] = insert_index
            # Set next on inserted element to point to old head
            self._buffer[insert_index + 1] = self._head
            # Update head to point to inserted element
            self._head = insert_index

    def pop(self):
        """Return element located at head of list, removing it from the list"""

        if self._head is None:
            raise IndexError("pop from empty list")

        cur_index = self._head

        data = self._buffer[self._head]

        if self._buffer[cur_index + 1]:
            self._head = self._buffer[cur_index + 1]
        else:
            self._head = None
            self._tail = None

        # allocate empty node to free stack
        if self._free_index:
            self._buffer[cur_index + 1] = self._free_index

        self._free_index = cur_index

        # Overwriting new free space not strictly needed, but useful for readability
        # Ensure prev is empty
        self._buffer[cur_index - 1] = None
        # Ensure value is empty
        self._buffer[cur_index] = 0

        self._count -= 1

        return data

    def __iter__(self):
        node_index = self._head
        while node_index is not None:
            # When yield statement is hit, program suspends execution
            # and returns yielded value to caller
            # When a function is suspended, the state of that function is saved.
            # This includes any variable bindings local to the generator, the instruction pointer,
            # the internal stack, and any exception handling.
            # This allows you to resume function execution whenever you call one of the generator’s methods
            yield self._buffer[node_index]
            node_index = self._buffer[node_index + 1]


if __name__ == "__main__":
    pass
