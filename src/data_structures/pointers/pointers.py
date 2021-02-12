'''Example of implementing linked list with pointers in an array

Usage: $ python3 pointers.py

'''


class LinkedListSingleArray:
    ''' A linked list implemented using a single array, with a custom pointer implementation
    '''

    def __init__(self, no_of_elements: int = 20):
        # Create an empty buffer (malloc), and populate 'pointer' to free elements
        self._buffer = [x + 2 if ( (x + 1) % 3 == 0) else 0 for x in range(0, no_of_elements*3)]
        self._free_index = 1
        self._current = None
        self._count = 0

    def __next__(self, index):

        if self._current is None:
            return None
        elif self._current + 1 is not None:
            return self._buffer[self._current + 1]
        else:
            return None

    def __len__(self):
        return self._count

    # def __getitem__(self, item):
    # def __current
    # def __iter__
    # def __prev
    # def __add
    # def __remove
    # def __contains__





    def __add__(self, other):
        self._buffer





if __name__ == '__main__':
    ARRAY_IN = [8, 0, 3, 3, 5, 6, 7]

    # heap_sort(ARRAY_IN)
