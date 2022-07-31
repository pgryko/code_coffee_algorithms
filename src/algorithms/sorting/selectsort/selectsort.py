def select_sort(array):

    for i in range(0, len(array)):
        j = i + 1
        # Second loop to find min value

        min_index = i
        while j < len(array):
            if array[min_index] > array[j]:
                min_index = j
            j = j + 1

        array[i], array[min_index] = array[min_index], array[i]


if __name__ == "__main__":
    array = [8, 0, 3, 3, 5, 6]

    select_sort(array)

    print(array)  # noqa
