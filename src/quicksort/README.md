Quicksort has a worst case running time of $`O(n^2)`$, but average $`O(nlgn)`$, with the cofactors in $`O(nlgn)`$ being quite small.

```
QuickSort(A,low,high)
    if low < high:
        mid = Partition(A,low,high)
        QuickSort(A,low,mid)
        QuickSort(A,mid+1,high)
```

Intialised with:

```
QuickSort(A,0,A.size-1)
```

The Partition function sorts the array in place:

```
Partition(A,low,high):
    key = A[high]
    i = low - 1
    for j = low to high -1:
        if A[j] <= key
            i = i + 1
            swap(A[i],A[j])
    swap (A[i+1],A[high])

    return i + 1
```