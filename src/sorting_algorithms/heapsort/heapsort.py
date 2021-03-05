'''Example of heapsort algorithem written in python

Usage: $ python3 heapsort.py

'''


def max_heapify(array, i: int = 0, size=None):
    '''
    Ensure that current node at i, is a maximum value with respect
    to its left and right leaf nodes,

    :param array: Array to be sorted
    :param i: Index of node in array
    :param size: Size of the heap to consider. We may want to mask values in the array
    that are larger than the specified size (to perform sorting)
    :return: None - sorts array in place
    '''

    # Initialise largest as root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if size is None:
        size = len(array)

    if left < size and array[left] > array[i]:
        largest = left

    if right < size and array[right] > array[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        # Ensure that sub tree maintains maxheap via recursive call
        max_heapify(array, largest, size)


def build_heap(array):
    '''
    Re-arrange an existing array/list into a maxheap
    Note, max heaps are loosely ordered, i.e. roots nodes
    are maximum's with respect to their leaf nodes. No other
    ordering guarantee is provided
    :param array:
    :return: None. sorts in place
    '''

    # operator // forces integer division (python 3)
    for i in range((len(array) - 1) // 2, -1, -1):
        max_heapify(array, i)


def heap_sort(array):
    '''
    Takes an existing array/list and re-arranges it into a max heap
    From there it iterates through the array, pulling out the max value (root)
    and running maxheapify to re-calculate the new max value
    :param array:
    :return: None, passed in array sorted in place
    '''
    if len(array) < 2:
        return

    # # Build heap (re-arrange array)
    # # range(start, stop, step)
    # # operator // forces integer division (python 3)
    for i in range((len(array) - 1) // 2, -1, -1):
        max_heapify(array, i)

    # We now have a max heap, one by one pull out the maximum element
    # and add it to the end of the array, and sort the remainder
    size = len(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]

        size = size - 1
        max_heapify(array, 0, size)


if __name__ == '__main__':
    ARRAY_IN = [8, 0, 3, 3, 5, 6, 7]

    heap_sort(ARRAY_IN)
