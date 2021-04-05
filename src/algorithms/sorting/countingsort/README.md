# Counting Sort

Comparative sorts (i.e. ones which require the comparisons of input elements) have a worst case lower limit complexity of
$`O(n \lg n)`$. In certain cases, such as working with integers, it is possible to sort in $`O(n)`$.

Counting sort takes an array of integers and returns a new array in $`O(n)`$.

```al
Counting-Sort(InArray, OutArray):

if OutArray.size != InArray:
   return error

// Find maximum integer value in Array
max_value  = findMaxValue(Array)

// Create comparison array of size max_value + 1
C = newArray[0...max_value]

// C contains a reference of the elements equal to i
for i = 0 to InArray.size - 1:
    C[Array[i]] = C[Array[i]]   

// C contains elemens less than or equal to i
for i = 1 to k:
    C[i] = C[i] + C[i-1]
    
for i = InArray.Size - 1 to 0:
    B[C[A[j]]] = A[j]
    C[A[j]] = C[A[j]] - 1
```