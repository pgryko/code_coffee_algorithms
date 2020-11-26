import copy


class MergeSort:
    """ Sorts an array using a recursive divide and concour strategy

    Technically we could write this as two nested functions, but I think its cleaner (design choice)
    to write it as a class. Its also easier to test, as testing a nested function is tricky
    """

    def __init__(self, array):
        """Sets off merge sort"""
        MergeSort.mergesort(array, 0, len(array) - 1)

    @staticmethod
    def merge(array, low, mid, high):
        lhs = copy.deepcopy(array[low:mid + 1])
        rhs = copy.deepcopy(array[mid + 1: high + 1])

        i = 0
        j = 0
        for k in range(low, high + 1):
            if i < len(lhs) and j < len(rhs):

                if lhs[i] <= rhs[j]:

                    array[k] = lhs[i]
                    i += 1
                else:
                    array[k] = rhs[j]
                    j += 1
            else:
                if i < len(lhs):
                    array[k] = lhs[i]
                    i += 1
                else:
                    array[k] = rhs[j]

    @staticmethod
    def mergesort(array, low, high):

        mid = int((low + high) / 2)

        if mid < high:
            MergeSort.mergesort(array, low, mid)
            MergeSort.mergesort(array, mid + 1, high)
            MergeSort.merge(array, low, mid, high)


if __name__ == '__main__':
    ARRAY_IN = [8, 0, 3, 3, 5, 6]

    MergeSort(ARRAY_IN)

    print(ARRAY_IN)
