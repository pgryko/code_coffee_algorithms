def MaxHeapify(array, i: int = 0, size=None):
    '''

    :param array: Array to be sorted
    :param size: Size of the heap
    :param i: Index of node in array
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
        MaxHeapify(array, largest, size)


def BuildHeap(array):
    # Build heap (re-arrange array)
    # range(start, stop, step)
    # operator // forces integer division (python 3)
    for i in range((len(array) - 1) // 2, -1, -1):
        MaxHeapify(array, i)


def HeapSort(array):
    if len(array) < 1:
        return

    # # Build heap (re-arrange array)
    # # range(start, stop, step)
    # # operator // forces integer division (python 3)
    for i in range((len(array) - 1) // 2, -1, -1):
        MaxHeapify(array, i)

    # We now have a max heap, one by one pull out the maximum element
    # and add it to the end of the array, and sort the remainder
    size = len(array)

    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]

        size = size - 1
        MaxHeapify(array, 0, size)


if __name__ == '__main__':
    array_in = [8, 0, 3, 3, 5, 6, 7]

    HeapSort(array_in)
