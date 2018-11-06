# InsertSort

Description

Input: A sequence of n numbers <a1, a2, a3,..., an>
Output: A permutation (reordering) <a1', a2', a3',...,an'> of the input sequence such that a1' <= a2' <= a3' <= ... < an'

The algorithm sorts numbers in place. Take the sequence
A = < 5, 2, 4, 6, 1, 3 >

1: for j = 2 to A.length
2:     key = A[j]
3:     i = j - 1
4:     while i > 0 and A[i] > key
5:         A[i+1] = A[i]
6:         i = i - 1
7:     A[i+1] = key

Output: A' = < 1, 2, 3, 4, 5, 6 >