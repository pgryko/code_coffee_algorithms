# HeapSort

## Description

An improved version of select sort, dividing its inputs into sorted and unsorted regions.
Like insert sort (but unlike merge sort), heapsort sorts in place.
This way it has the best of both algorithms. Complexity O(nlogn)


Heaps are also an efficient datastructures for priority queues and is used in garbage-collected programming languages.
They are partially filled binary trees, with a max heap having its largest value at the root (top).

```mermaid
graph TD
    1((16)) --- 2((14))
    1((16)) --- 3((10))
    2 --- 4((8))
    2 --- 5((7))
    4 --- 8((2))
    4 --- 9((4))
    5 --- 10((1))
    3 --- 6((9))
    3 --- 7((3))
```

This tree has a height of 3 and can be represented as an array:

```mermaid
graph TD
    subgraph array
    16
    14
    10
    8
    7
    9
    3
    2
    4
    1
    end
```

Accessing adjacent elements can be performed, with

Parent(i) return $`\lfloor i/2 \rfloor`$

Left(i) return $`2i`$

Right(i) return $`2i + 1`$

## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./mergesort

Or manually using g++
$ g++ --std=c++1z main.cpp