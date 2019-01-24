# InsertSort


# Description

Input: A sequence of n numbers <a1, a2, a3,..., an>
Output: A permutation (reordering) <a1', a2', a3',...,an'> of the input sequence such that a1' <= a2' <= a3' <= ... < an'

The algorithm sorts numbers in place. Take the sequence
A = < 5, 2, 4, 6, 1, 3 >

```
                                    cost    times
1: for i = 2 to A.length            c_1     n
2:     key = A[i]                   c_2     n - 1
3:     j = i - 1                    c_3     n - 1
4:     while j > 0 and A[j] > key   c_4     $`\sum^n_j=2 t_j`$
5:         A[j+1] = A[j]            c_5     \sum^n_j=2 t_j - 1
6:         j = j - 1                c_6     \sum^n_j=2 t_j - 1
7:     A[j+1] = key                 c_7     n - 1
```

To calculate runtime T(n) we sum up the running times of cost and times.
```math
T(n) = nc_1 + (n - 1)c_2 + (n - 1)c_3 + (n - 1)c_3 + \sum^n_{j=2} t_jc_4 + (t_j - 1)c_5 + (t_j - 1)c_6
```

Best case scenario - array is already sorted, $`t_j = 1`$

```math
T(n) = nc_1 + (n - 1)c_2 + (n - 1)c_3 + (n-1)c_4 + (n-1)c_7
T(n) = n(c_1 + c_2 + c_3 + c_4 + c7) - (c_2 + c_3 + c_4 + c_7)
```

I.e. an+b, hence liner time

Worst case, reverse order

```math

```


Output: A' = < 1, 2, 3, 4, 5, 6 >

When working with array indexes starting at zero

```
1: for i = 1 to A.length - 1
2:     key = A[i]
3:     j = i - 1
4:     while j != 0 and A[j] > key
5:         A[j + 1] = A[j]
6:         j = j -1
7:     A[j + 1] = key
```

# Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./insertsort
