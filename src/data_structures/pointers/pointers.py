'''Example of implementing linked list with pointers in an array

Usage: $ python3 pointers.py

'''


# https://omkarpathak.in/2018/04/11/python-getitem-and-setitem/
class LinkedListSingleArray:
    ''' A doubly linked list implemented using a single array, with a custom pointer implementation

    A stack is used as a free list to keep track of free space in allocated buffer.
    Buffer is doubled in size of element is pushed beyond container capacity
    '''

    def __init__(self, capacity: int = 20):

        # Make sure capacity is greater than 1, otherwise
        # resize function will fail
        if capacity < 1:
            capacity = 2
        # Create an empty buffer (malloc), and populate 'pointer' to free elements
        # Buffer array is partitioned into blocks of 3, with |prev, key, next|
        # e.g.
        # [|prev,key,next|, |prev, key, next|, |prev, key, next| ]
        # where the 'pointers', point to the next/prev key
        # e.g for an empty array [None, 0, 4, None, 0, 7, None, 0, None]
        self._buffer = [x + 2 if ((x + 1) % 3 == 0) else 0 if ((x + 2) % 3 == 0)
        else None for x in range(0, capacity * 3)]
        # Set end element to None
        self._buffer[-1] = None
        self._free_index = 1
        self._current = None
        self._count = 0
        self._head = None
        self._tail = None

    def __next__(self, index):

        if self._current is None:
            return None
        elif self._current + 1 is not None:
            return self._buffer[self._current + 1]
        else:
            return None

    def __len__(self):
        return self._count

    def capacity(self):
        return len(self._buffer) // 3

    def _resize(self):
        '''Increase the size of the array buffer and
        update free list. Different implementations have a different scalar factors,
        either 2x or 1.5 based on assumptions made in amortized analysis.
        Here we just double the size of the buffer
        '''
        init_size = len(self._buffer)

        self._buffer.extend([x + 2 if ((x + 1) % 3 == 0) else 0 if ((x + 2) % 3 == 0) else None for x in range(init_size, init_size*2)])
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

    def _get_next_index(self,current_index):
        '''Helper function to get index of next element
        '''

        if (current_index + 2) % 3 != 0:
            raise IndexError('Index does not appear to be valid')

        return self._buffer[current_index + 1]

    def _get_prev_index(self,current_index):
        '''Helper function to get index of prev element
        '''

        if (current_index + 2) % 3 != 0:
            raise IndexError('Index does not appear to be valid')

        return self._buffer[current_index - 1]


    def push(self, element):
        '''Insert an element into the list
        '''

        if self._free_index is None:
            self._resize()

        insert_index = self._free_index

        next_free = self._get_next_index(self._free_index)
        # Insert element into location of current free element

        self._buffer[insert_index] = element
        # As element is set to head of list, set next to None
        self._buffer[insert_index - 1] = None
        # Update free list
        self._free_index = next_free

        if self._head is None:
            self._head = insert_index
            self._buffer[insert_index + 1] = None
        else:
            self._buffer[insert_index + 1] = self._head
            self._head = insert_index

    def remove(self, index):
        '''Remove an element at a specific location'''
        pass

    def pop(self):
        '''Return element located at end/tail of list, removing it from the list'''
        pass

    # def __getitem__(self, item):
    # def __current
    # def __iter__
    # def __prev
    # def __add
    # def __remove
    # def __contains__

    def __add__(self, other):
        pass


if __name__ == '__main__':
    pass
