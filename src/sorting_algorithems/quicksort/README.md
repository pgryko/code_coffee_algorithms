Quicksort has a worst case running time of $`O(n^2)`$, but average $`O(nlgn)`$, with the cofactors in $`O(nlgn)`$ being quite small.

```
QuickSort(A,low,high)
    // Optional add in check that high !=  numeric lits
    if low < high:
        p = Partition(A,low,high)
        QuickSort(A,low,p-1)
        QuickSort(A,p+1,high)
```

If using an unsinged int, make sure to add additional check in low < high && high != numericlimit::max

Intialised with:

```
QuickSort(A,0,A.size-1)
```

The Partition function sorts the array in place:

```
Partition(A,low,high):
    pivot = A[high]
    i = low - 1
    for j = low to high -1:
        if A[j] <= pivot
            i = i + 1
            swap(A[i],A[j])
    swap (A[i+1],A[high])

    return i + 1
```


## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./mergesort

Or manually using g++
$ g++ --std=c++1z main.cpp