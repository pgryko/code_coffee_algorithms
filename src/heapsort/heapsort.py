def MaxHeapify(array, size, i):
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

    if left < size and array[left] > array[i]:
        largest = left

    if right < size and array[right] > array[i]:
        largest = right

    # If largest is not root
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        MaxHeapify(array, i, 0)


def HeapSort(array):
    if len(array) < 2:
        return

    # Build heap (re-arrange array)
    # range(start, stop, step)
    # operator // forces integer division (python 3)
    for i in range(len(array) // 2 - 1, -1, -1):
        MaxHeapify(array, len(array), i)

    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        MaxHeapify(array, len(array), i)


if __name__ == '__main__':
    array_in = [8, 0, 3, 3, 5, 6, 7]

    HeapSort(array_in)

    print(array_in)
