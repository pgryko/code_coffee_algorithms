# -*- coding: utf-8 -*-
"""Quicksort implementation in python

Sorts an array type object in place, in approx time O(nlgn)

Example usage:
    QuickSort(ARRAY_IN)

"""


class QuickSort:
    """Class that initialises and wraps functions that perform quicksort in approx O(nlgn)"""

    def __init__(self, array):
        """Kicks off QuickSort
        Args:
            array (:obj:`list` of int): array to be sorted
        """
        self._quicksort(array, 0, len(array) - 1)

    @staticmethod
    def _partition(array, low, high):
        """
        There are many different versions of quickSort that pick pivot in different ways.

        Always pick first element as pivot.
        Always pick last element as pivot (implemented below)
        Pick a random element as pivot.
        Pick median as pivot.

        :param array:
        :param low:
        :param high:
        :return: int: integer specifying partition index
        """
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    @staticmethod
    def _quicksort(array, low, high):
        """Private static member function that performs quicksort in a recursive manner

        :param array:
        :param low:
        :param high:
        :return:
        """

        if low < high:
            partition = QuickSort._partition(array, low, high)
            QuickSort._quicksort(array, low, partition - 1)
            QuickSort._quicksort(array, partition + 1, high)

        return array


if __name__ == "__main__":
    ARRAY_IN = [5, 4, 2, 1, -6, 3, 1]

    QuickSort(ARRAY_IN)

    print(ARRAY_IN)  # noqa
