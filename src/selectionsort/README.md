# Selection Sort

# Description

Find the first smallest element in the array and exchange it with the first. Next find the second smallest element in the array and exchange it with the second. Continue until array is sorted

Called selection sort, as it works by repeatedly selecting the smallest element.

Approx ~N^2/2 compares and N exchanges.

For each i from 0 to N - 1, there is one exchange and N - 1 - i compares.
So the totals are (N - 1) + (N - 2) + (N - 3) .. + 2 + 1 = N(N - 1)/2 ~ N/2 Compares

- Runtime is insensitive to input
- Data movement is minimal. N exchanges for N elements, linear in growth

```
1: for i = 0 to A.length - 1
2:   min_index = i
3:   for j = i + 1 to A.length - 1:
4:      if a[j] < a[i]
5:			min_index = j
6:	 swap(a[i], a[min_index])

```

# Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./selectsort
