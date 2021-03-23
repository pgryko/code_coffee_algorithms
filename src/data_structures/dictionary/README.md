# Dynamic sets

Dictionaries are dynamic sets, which support element insertion, deletion and querying.

A hash function h(k) is used to map a key k to a location in a data structure.
Hash collisions, where $ k_1 \neq k_2 $ but $ h(k_1) = h(k_2) $, are delt with by entering the keys into a linked list. This is called chasing with chainging. For n keys and m slots, the probability of a colision under the assumption of uniform hashing is $ n/m =  \alpha$, where $\alpha$ is known as the load function. The complexity is $O(1 + \alpha)$, where an $O(1)$ is always performed as part of the pre-hashing.

## Hashing functions

https://www.youtube.com/watch?v=0M_kIqhwbFo
https://www.youtube.com/watch?v=BRO7mVIFt08

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

A should be odd, and

We perform a binary multiplication of $k \times A \cdot 2^\omega$ , resulting in a value $r_12^\omega + r_0$ which has length $2 \omega$. Knuth suggests the constant of  

```math
A \approx (\sqrt5 -1)/2 \approx 0.618 
```

3. Universal Hasing:

```math
h(k) = [(ak + b) \mod p] mod m
```

mod m at end, division methond to make sure that result is between zero and m -1.
A and b are random numbers between {0...,p-1}, where p is prime >|U|. 

for worst case keys $ k_1 \neq k_2 $, Probability{$h(k_1) = h(k_2)$} = 1/m

Probability arrises from $P(a \cap b)$

4. Rolling hash ADT, Karp-Rabin Algorithem

Used in Substring search problem. Possible to use division methon

```math
h(k) = k \mod m
```

provided m is a random prime number greater than string S

treat string s as a multidigit number U in base a (which the size of your alphabet)