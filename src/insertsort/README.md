# InsertSort


# Description

Input: A sequence of n numbers <a1, a2, a3,..., an>
Output: A permutation (reordering) <a1', a2', a3',...,an'> of the input sequence such that a1' <= a2' <= a3' <= ... < an'

The algorithm sorts numbers in place. Take the sequence
A = < 5, 2, 4, 6, 1, 3 >

```
1: for i = 2 to A.length
2:     key = A[i]
3:     j = i - 1
4:     while j > 0 and A[j] > key
5:         A[j+1] = A[j]
6:         j = j - 1
7:     A[j+1] = key
```

Output: A' = < 1, 2, 3, 4, 5, 6 >

When working with array indexes starting at zero

```
1: for i = 1 to A.length - 1
2:     key = A[i]
3:     j = i - 1 
4:     while j > 0 and A[j] > key
5:         A[j + 1] = A[j]
6:         j = j -1
7:     A[j + 1] = key
```

# Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./insertsort