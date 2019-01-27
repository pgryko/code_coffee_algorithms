# Merge Sort

# Description

Takes a divide and conquer approach to sorting.

*Divide* the n-elements into subarrays of n/2
*Sort* the two subsequences using mergesort
*Merge*  the two sorted sequences to produce a sorted answer

The merge procedure Merge(A,p,q,r), where A is the input array, p,q,r are indexes, where $'p <= q < r'$

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
