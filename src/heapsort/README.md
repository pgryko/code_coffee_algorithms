# Merge Sort

## Description

Takes a divide and conquer approach to sorting.

*Divide* the n-elements into sub-arrays of n/2
*Sort* the two sub-sequences using merge-sort
*Merge*  the two sorted sequences to produce a sorted answer


An initial call to merge sort is called with Merge-Sort(A,1,A.length)
```
Merge-Sort(A, p, r)

1: if p < r
2:    q = [(p+r)/2)]
3:    Merge-Sort(A,p,q)
4:    Merge-Sort(A,q+1,r)
5:    Merge(A,p,q,r)

```

The merge procedure Merge(A,p,q,r), where A is the input array, p,q,r are indexes, where $'p <= q < r'$.

The procedure assumes sub arrays [p..q] and [q+1...r] are correctly sorted and merges them to replace [p...r]

```
Merge(A,p,q,r)

1: n_1 = q - p + 1
2: n_2 = r - q
3: Let L[1..n_1 + 1] and R[1..n_2 + 1] be new arrays
4: For i = 1 to n_1
5:    L[i] = A[p + i -1]
6: For j = 1 to n_2
7:    R[j] = A[q + j]
8: L[n_1 + 1] = infinity
9: R[n_2 + 1] = infinity
10: i = 1
11: j = 1
12: for k = p to r
13:    if L[i] <= R[j]
14:       A[k] = L[i]
15:       i = i + 1
16:    else A[k] = R[j]
17:        j = j + 1
```

In detail, Line 1 computes the length $`n_1`$ of the sub array A[p..q], and line 2 the length $`n_2`$ of the sub array A[q+1..r]. We create subarrays of lengths $`n_1 + 1`$ and $`n_2 + 1`$ respectively. The extra position holds a 'sentinel' marker.

The for loops of lines 4-5 copies the sub-array A[p..q] into $`L[1..n_1]`$, and lines 6-7 copies the sub-array A[q + 1..r] into $`R[1..n_2]`$. Lines 8 & 9 put sentinels into the ends of the sub arrays.

In the for loops for lines 12-17, the subarray, 

## Runtime

Merge procedure runs in approx O(n) time

$``T(n) = 2T(n/2) + O(n) if n > 1``$

Through analysing the recursion tree, its possible to show algorithm is O(nlogn)

## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./mergesort

Or manually using g++
$ g++ --std=c++1z main.cpp