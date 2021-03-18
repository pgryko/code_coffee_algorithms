# Dynamic sets

Dictionaries are dynamic sets, which support element insertion, deletion and querying.

## Hashing functions

https://www.youtube.com/watch?v=0M_kIqhwbFo

1 Division method:

Map key k into m slots by taking the remainder of k divided by m.

```math
h(k) = k \mod m
```

Need to avoid certain numbers for m, such as 2 or 10. Ideally m should be a prime number to avoid common factors for k and m.

2 Multiplication 

Multiple key k byt constant A (0< A < 1) and extract the fractional part of kA. Then multiply this value by m and take the floor of the result.

```math
h(k) \lfloor m (k A mod 1) \rfloor
```

where $k A \mod 1$ means take the fractional part of kA, i.e $ kA - \lfloor KA \rfloor$.

For implementation, we typically choose the value of m to be a power of 2 ( $m = 2^p$ for some integer $p \in \mathbb{N}$)

For a key k that is $\omega$ bits long, we restrict A to be a fraction, in the form $s/2^\omega$, where s in an integer int he range $0<s<2^2$.

```math
h(k) = [ (a.k) \mod 2^w]
```

We perform a binary multiplication of $k \times A \cdot 2^\omega$ , resulting in a value $r_12^\omega + r_0$ which has length $2 \omega$. Knuth suggests the constant of  

```math
A \approx (\sqrt5 -1)/2 \approx 0.618 
```
