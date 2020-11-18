# HeapSort

## Description

An improved version of select sort, dividing its inputs into sorted and unsorted regions.
Like insert sort (but unlike merge sort), heapsort sorts in place.
This way it has the best of both algorithms.

Heaps are also an efficient datastructures for priority queues and is used in garbage-collected programming languages.

Complexity O(nlogn)
## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./mergesort

Or manually using g++
$ g++ --std=c++1z main.cpp