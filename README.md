# self_study

A collection of small projects for self study. The goal is to use these for teaching in Code & Coffee meetups

Aim is to work through standard algorithm, data structures questions in both python and C++ (both languages due to differences in the way memory is managed).

- [x] Support Tasks
  - [x] Get Unit tests working
  - [x] Get Math rendering working
- [ ] Math
  - [ ] Sum of finite series
  
- [ ] Algorithms
  - [ ] Sorting
    - [x] Insert Sort
    - [x] Select Sort
    - [x] Merge Sort (nlogn)
    - [ ] Heap Sort (nlogn) sorts in place

- [ ] Data structures
  - [ ] Bloom filter (http://blog.amynguyen.net/?p=853)
  - [ ] Ternary search tree
  - [ ] Prefix trie (replaced by ternary search trees, does not require wasting memory storing 26 pointers at each node)
  - [ ] Suffix array
  - [ ] T/Q Digest
  - [ ] Count-min sketch
  - [ ] Dense/sparse matrix-matrix multiplication 
  - [ ] Lazy/streaming algorithm

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

- Suggested list of topics
    https://medium.com/educative/3-month-coding-interview-bootcamp-904422926ce8

- Practical Cryptography for developers
    https://cryptobook.nakov.com/

- Things every software engineer should know
    https://github.com/mtdvio/every-programmer-should-know

- Problem Solving with Algorithms and Data Structures using Python
    http://interactivepython.org/runestone/static/pythonds/index.html

- Video lectures on 4 algorithmic journeys
  https://www.youtube.com/user/A9Videos/playlists

- Books
  TCP/IP Illustrated Volume 1
  The Design of the UNIX Operating System
# Building & Run instructions:

Git clone recursively

$ git clone --recursive git@gitlab.com:pgryko/self_study.git

This is as we use google test library as a git submodule 

## CPP

Dependencies:

```bash

$ sudo apt install gcc cmake googletest
```

For Ubuntu you need to install and compile the libs yourself
```bash
$ sudo apt install libgtest-dev
$ cd /usr/src/gtest
$ sudo cmake CMakeLists.txt
$ sudo make
$ sudo cp *.a /usr/lib
```

```bash
$ cmake -H. -Bbuild
$ cd build
$ make
$ ./unit_tests
```

Or manually using g++
```bash
$ g++ --std=c++1z main.cpp
```

### Debugging

Core dumps need to be enabled via
```shell
$ ulimit -c unlimited
```

g++ debugging symbols also need to be enabled. This can be done via either adding in '-g' when calling gcc or adding set(CMAKE_BUILD_TYPE Debug) to cmake

It should then be possible to debug your executable using gdb

```shell
$ gdb binary core
```
## Python
Dependencies:

```bash

$ sudo apt install python3-pip python3-venv
```

```bash
$ pytest
```
## Docker
```bash
$ sudo docker build -t self_study .
$ sudo docker run self_study
```
This will terminate upon completion. To create an interactive session:
```bash
$ sudo docker run  --name self_study -d self_study tail -f /dev/null --stop-timeout 600
$ sudo docker exec -it self_study /bin/bash
```

