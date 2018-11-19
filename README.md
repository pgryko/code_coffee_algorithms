# self_study

A collection of small projects for self study

Aim is to work through standard algorithm, data structures questions in both python and C++ (both languages due to differences in the way memory is managed).

- [x] Get Unit tests working
- [ ] Insert Sort
- [ ] Merge Sort
# Study references:

- Problem Solving with Algorithms and Data Structures using Python
  http://interactivepython.org/runestone/static/pythonds/index.html

- Data Open structures in C++
  http://opendatastructures.org/ods-cpp/

- The Algorithms Design Manual

  http://www3.cs.stonybrook.edu/~skiena/373/videos/

  http://www.algorist.com/algowiki/index.php/The_Algorithms_Design_Manual_(Second_Edition)

 - Examples of algorithm implementations
  https://www.geeksforgeeks.org/

# Building & Run instructions:

## CPP

$ cmake -H. -Bbuild
$ cd build
$ make
$ ./unit_tests

## Python

$ pytest
