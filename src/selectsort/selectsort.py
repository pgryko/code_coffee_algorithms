def select_sort(array):
    def swap_values(array, index, min_index):

        temp_val = array[min_index]
        array[min_index] = array[index]
        array[index] = temp_val

    for i in range(0, len(array)):
        j = i + 1
        # Second loop to find min value

        min_index = i
        while j < len(array):
            if array[min_index] > array[j]:
                min_index = j
            j = j + 1

        swap_values(array, i, min_index)


if __name__ == '__main__':
    array = [8, 0, 3, 3, 5, 6]

    select_sort(array)

    print(array)
