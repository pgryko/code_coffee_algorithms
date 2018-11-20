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

 - Suggested list of topics
   https://medium.com/educative/3-month-coding-interview-bootcamp-904422926ce8

# Building & Run instructions:

Git clone recursively

$ git clone --recursive git@gitlab.com:pgryko/self_study.git

This is as we use google test library as a git submodule 

## CPP
```bash
$ cmake -H. -Bbuild
$ cd build
$ make
$ ./unit_tests
```
## Python
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