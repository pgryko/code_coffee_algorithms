import copy


class merge_sort(object):

    def __init__(self, array):
        '''Sets off merge sort'''
        merge_sort.__merge_sort(array, 0, len(array) - 1)

    @staticmethod
    def merge(array, low, mid, high):
        lhs = copy.deepcopy(array[low:mid+1])
        rhs = copy.deepcopy(array[mid + 1: high + 1])
        print(str(low) + " " + str(mid) + " " + str(high))

        print("Merging")

        print("lhs")
        print(lhs)
        print("rhs")
        print(rhs)

        i = 0
        j = 0
        for k in range(low, high+1):
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

    def __merge_sort(array, low, high):

        mid = int((low + high)/2)

        if mid < high:
            merge_sort.__merge_sort(array, low, mid)
            merge_sort.__merge_sort(array, mid+1, high)
            merge_sort.merge(array, low, mid, high)


if __name__ == '__main__':
    array = [8, 0, 3, 3, 5, 6]

    merge_sort(array)

    print(array)
