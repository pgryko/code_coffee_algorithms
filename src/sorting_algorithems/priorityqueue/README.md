A priority queue is a data structure based off a [max heap](../mergesort/README.md) for maintaining a set S of elements with and associated key value. A max-priority queue supports the following:

Insert(S,x) inserts the element x into the set S, which is equivalent to operation $`S = S \cup \left \{ x \right \}`$

Maximum(S) returns element S with largest key.

Extract-Max(S) removes and returns the element of S with the largest key.

Increase-Key(S,x,k) increases the value of elements x's key to new value k, where k > key[x]

In addition to the [maxheap, buildheap](../mergesort/README.md) functions, we need

```
Heap-Maximum(A): return A[0]
```

```
Heap-Extract-Max(A):
if A.heapsize < 1:
    throw error
max = A[0]
A[0] = A[A.heapsize - 1]
heapsize = A.heapsize - 1
Max-Heapify(A,0,heapsize)

return max
```

Runtime of Heap-Extract-Max is O(lg n), since it Max-heapify is run only once.

```
Heap-Increase-Key(A,i,key):
if key < A[i]:
    throw error
A[i] = key
while i > 1 and A[Parent(i)] < A[i]
    swap(A[i],A[Parent(i)])
    i = Parent(i)
```

```
Max-Heap-Insert(A,key)
heapsize = heapsize + 1
A[A.heapsize -1 ] = null 
Heap-Increase-Key(A,heapsize,key)
```