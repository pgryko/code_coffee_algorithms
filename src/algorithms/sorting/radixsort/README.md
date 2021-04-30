# Radix Sort

Radix sort is a non comparative sort, that sorts based of a number position (radix or base).
It avoids comparison by creating and distributing elements according to their radix.

Radix sort can be applied to data that can be sorted lexicograpically (e.g. integers, words, punch cards, playing cards, mail)

Complexity is `$O(nw)$` where n is number of keys and k is the key length.

Radix sort can start from the least significant digit (LSD) or most significant digit (MSD).

The LSD algorithm sorts by the least significant digit while preserving relative order, then the next significant digit. LSD requires the use of a stable sort (one that maintains relative order for same keys), the MSD does not (but itself is not a stable sort).

Counting sort is commonly used as the internal stable sort used by radix. Hybrid approaches, that use insert sort for small bins, improve performance significantly

```math
\begin{matrix}
 3&  2& 9\\ 
 4&  5& 7\\ 
 6&  5& 7\\ 
 8&  3& 9\\ 
 4&  3& 6\\ 
 7&  2& 0\\ 
 3&  5& 5
\end{matrix}
\quad \rightarrow \quad 
\begin{matrix}
 7&  2& \colorbox{#D3D3D3}{0}\\ 
 3&  5& \colorbox{#D3D3D3}{5}\\ 
 4&  3& \colorbox{#D3D3D3}{6}\\ 
 4&  5& \colorbox{#D3D3D3}{7}\\ 
 6&  5& \colorbox{#D3D3D3}{7}\\ 
 3&  2& \colorbox{#D3D3D3}{9}\\ 
 8&  3& \colorbox{#D3D3D3}{9}
\end{matrix}
\quad \rightarrow \quad 
\begin{matrix}
 7&  \colorbox{#D3D3D3}{2}& 0\\ 
 3&  \colorbox{#D3D3D3}{2}& 9\\ 
 4&  \colorbox{#D3D3D3}{3}& 6\\ 
 8&  \colorbox{#D3D3D3}{3}& 9\\ 
 3&  \colorbox{#D3D3D3}{5}& 5\\ 
 4&  \colorbox{#D3D3D3}{5}& 7\\ 
 6&  \colorbox{#D3D3D3}{5}& 7
\end{matrix}
\quad \rightarrow \quad
\begin{matrix}
 \colorbox{#D3D3D3}{3}&  2& 9\\ 
 \colorbox{#D3D3D3}{3}&  5& 5\\ 
 \colorbox{#D3D3D3}{4}&  3& 6\\ 
 \colorbox{#D3D3D3}{4}&  5& 7\\ 
 \colorbox{#D3D3D3}{6}&  5& 7\\ 
 \colorbox{#D3D3D3}{7}&  2& 0\\ 
 \colorbox{#D3D3D3}{8}&  3& 5
\end{matrix}
```

```al
Radix-Sort(A,d):
for i = 0 to d - 1
    stable sort array A on digit i
```