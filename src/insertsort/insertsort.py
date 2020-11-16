def insert_sort(array):
    for i in range(1, len(array)):
        j = i - 1

        key = array[i]

        while j > -1 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


if __name__ == '__main__':
    array = [8, 0, 3, 3, 5, 6]

    insert_sort(array)

    print(array)
