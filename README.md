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
    - [x] Insert Sort (On^2)
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

- Concise collection of high value information on specific application security topics
    https://cheatsheetseries.owasp.org/

- Video lectures on 4 algorithmic journeys
  https://www.youtube.com/user/A9Videos/playlists

- Books
  TCP/IP Illustrated Volume 1
  The Design of the UNIX Operating System

- Miscellaneous blogs
  - Overview of math in datascience
    https://www.dataquest.io/blog/math-in-data-science/

  - Short tutorials on timeseries forecasting
    https://news.ycombinator.com/item?id=20253622
    https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
    https://kanoki.org/2020/04/30/time-series-analysis-and-forecasting-with-arima-python/

  - Illustrated guide to Flask, Celery & Redis
    https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/

  - Postgres internals
    http://www.interdb.jp/pg/index.html
    https://news.ycombinator.com/item?id=18950460
    https://architecture-database.blogspot.com
    https://cstack.github.io/db_tutorial/
    https://www.youtube.com/watch?v=wTPGW1PNy_Y
    
  - The genius of bees https://www.epsilontheory.com/three-body-problem/
  
  - Object-oriented design patterns in the Linux kernel https://news.ycombinator.com/item?id=18410565 
   
  - Building a real-time colaborative text editor http://digitalfreepen.com/2017/10/06/simple-real-time-collaborative-text-editor.html
   
  - Schedualing in Golang https://www.ardanlabs.com/blog/2018/08/scheduling-in-go-part2.html
# Building & Run instructions:

Git clone recursively

$ git clone --recursive git@gitlab.com:pgryko/self_study.git

This is as we use google test library as a git submodule 

## CPP

Dependencies:

```bash

$ sudo apt install gcc cmake libgtest-dev
```

For Ubuntu you need to install and compile the libs yourself. It is not recommend to install a pre-compiled version of google test (for example into /usr/local) as [described by this note from google](https://github.com/google/googletest/blob/36066cfecf79267bdf46ff82ca6c3b052f8f633c/googletest/docs/faq.md#why-is-it-not-recommended-to-install-a-pre-compiled-copy-of-google-test-for-example-into-usrlocal)

```bash
$ cd external/googletest
```

if the folder does not exist, then you did not do a "--recursive" git clone earlier, which can be fixed with:

```bash
$ git submodule update --init --recursive
```

then in the directory external/googletest, run

```bash
$ cmake CMakeLists.txt
$ make
$ cd ../..
```

If you want to install the google test libs into /usr/local/lib, copy the contents of
```bash
$ sudo cp external/googletest/lib/libgtest*.a /usr/local/lib
``` 

In the project root directory (top folder)

```bash
$ cmake -H. -Bbuild
$ cd build
$ make
$ ./unit_tests
```

Or manually using g++ (if you have google tests copied into /usr/local/lib)
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
$ docker build -t self_study .
$ docker run --rm self_study
```
This will terminate upon completion. To create an interactive session:
```bash
$ docker run -it --rm self_study /bin/bash
```

